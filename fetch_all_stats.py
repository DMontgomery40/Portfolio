#!/usr/bin/env python3
"""
Fetch ALL package statistics for a user across npm, PyPI, and GitHub
No hardcoded package names - discovers everything automatically!
Uses only standard library - no external dependencies
"""

import urllib.request
import urllib.parse
import json
from datetime import datetime
import subprocess
import ssl

# Create SSL context for HTTPS requests
ssl_context = ssl.create_default_context()


def fetch_url(url, headers=None):
    """Helper to fetch URL with proper headers"""
    req = urllib.request.Request(url)
    if headers:
        for key, value in headers.items():
            req.add_header(key, value)
    try:
        with urllib.request.urlopen(req, context=ssl_context, timeout=10) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"    Error fetching {url}: {e}")
        return None


def get_npm_stats(username='dmontgomery40'):
    """Fetch ALL npm packages and their download stats"""
    print(f"\n📦 Fetching NPM stats for {username}...")
    
    total_downloads = 0
    packages_found = []
    
    try:
        # Method 1: Try npm CLI to list all packages by the user
        print(f"  Searching for packages by {username}...")
        result = subprocess.run(
            ['npm', 'search', '--json', f'maintainer:{username}'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0 and result.stdout:
            try:
                packages_data = json.loads(result.stdout)
                for pkg in packages_data:
                    package_name = pkg.get('name', '')
                    if package_name:
                        packages_found.append(package_name)
                        print(f"  Found package: {package_name}")
            except json.JSONDecodeError:
                print("    Could not parse npm search results")
        
        # Also try with author search
        result2 = subprocess.run(
            ['npm', 'search', '--json', f'author:{username}'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result2.returncode == 0 and result2.stdout:
            try:
                packages_data = json.loads(result2.stdout)
                for pkg in packages_data:
                    package_name = pkg.get('name', '')
                    if package_name and package_name not in packages_found:
                        packages_found.append(package_name)
                        print(f"  Found package: {package_name}")
            except:
                pass
    
    except subprocess.TimeoutExpired:
        print("  npm search timed out")
    except Exception as e:
        print(f"  Error running npm search: {e}")
    
    # Get download stats for each package found
    for package_name in packages_found:
        try:
            # Get last year downloads (more reliable than all-time)
            stats_url = f"https://api.npmjs.org/downloads/point/last-year/{package_name}"
            data = fetch_url(stats_url)
            if data and 'downloads' in data:
                downloads = data['downloads']
                total_downloads += downloads
                print(f"    {package_name}: {downloads:,} downloads (last year)")
        except Exception as e:
            print(f"    Could not fetch stats for {package_name}")
    
    return {
        'total_downloads': total_downloads,
        'packages': packages_found,
        'package_count': len(packages_found)
    }


def get_pypi_stats(username='DMontgomery40'):
    """Fetch ALL PyPI packages and their download stats"""
    print(f"\n🐍 Fetching PyPI stats for {username}...")
    
    total_downloads = 0
    packages_found = []
    
    try:
        # Get GitHub repos to check for Python packages
        github_url = f"https://api.github.com/users/{username}/repos?per_page=100"
        repos_data = fetch_url(github_url, headers={'Accept': 'application/vnd.github.v3+json'})
        
        if repos_data:
            for repo in repos_data:
                repo_name = repo.get('name', '').lower()
                
                # Try different naming conventions
                possible_names = [
                    repo_name,
                    repo_name.replace('_', '-'),
                    repo_name.replace('-', '_'),
                ]
                
                for pkg_name in possible_names:
                    try:
                        # Check if package exists on PyPI
                        pypi_url = f"https://pypi.org/pypi/{pkg_name}/json"
                        pkg_data = fetch_url(pypi_url)
                        
                        if pkg_data and pkg_name not in packages_found:
                            packages_found.append(pkg_name)
                            print(f"  Found package: {pkg_name}")
                            
                            # Get info about the package
                            info = pkg_data.get('info', {})
                            author = info.get('author', '')
                            if username.lower() in author.lower():
                                print(f"    Confirmed author match: {author}")
                            
                            # Try to get download stats from pypistats
                            try:
                                stats_url = f"https://pypistats.org/api/packages/{pkg_name}/recent"
                                stats_data = fetch_url(stats_url)
                                if stats_data and 'data' in stats_data:
                                    last_month = stats_data['data'].get('last_month', 0)
                                    total_downloads += last_month * 12  # Rough annual estimate
                                    print(f"    Downloads (last month): {last_month:,}")
                            except:
                                # If pypistats fails, just count that we found the package
                                print(f"    Package found but stats unavailable")
                            
                            break  # Found this repo as a package, no need to try other names
                    except:
                        continue
    
    except Exception as e:
        print(f"  Error: {e}")
    
    return {
        'total_downloads': total_downloads,
        'packages': packages_found,
        'package_count': len(packages_found)
    }


def get_github_stats(username='DMontgomery40'):
    """Fetch ALL GitHub repository statistics"""
    print(f"\n🐙 Fetching GitHub stats for {username}...")
    
    total_stars = 0
    total_forks = 0
    total_watchers = 0
    total_issues = 0
    repos_found = []
    languages = {}
    
    try:
        # Get all repos (handle pagination)
        page = 1
        while page <= 10:  # Safety limit
            github_url = f"https://api.github.com/users/{username}/repos?per_page=100&page={page}"
            repos_data = fetch_url(github_url, headers={'Accept': 'application/vnd.github.v3+json'})
            
            if not repos_data:
                break
                
            for repo in repos_data:
                repo_name = repo.get('name', 'Unknown')
                stars = repo.get('stargazers_count', 0)
                forks = repo.get('forks_count', 0)
                watchers = repo.get('watchers_count', 0)
                open_issues = repo.get('open_issues_count', 0)
                language = repo.get('language', 'Unknown')
                
                repos_found.append(repo_name)
                total_stars += stars
                total_forks += forks
                total_watchers += watchers
                total_issues += open_issues
                
                if language and language != 'Unknown':
                    languages[language] = languages.get(language, 0) + 1
                
                if stars > 0 or forks > 0:
                    print(f"  {repo_name}: ⭐ {stars} | 🍴 {forks}")
            
            if len(repos_data) < 100:
                break
            page += 1
    
    except Exception as e:
        print(f"  Error fetching repos: {e}")
    
    # Get user info for followers
    followers = 0
    following = 0
    public_repos = 0
    
    try:
        user_url = f"https://api.github.com/users/{username}"
        user_data = fetch_url(user_url, headers={'Accept': 'application/vnd.github.v3+json'})
        if user_data:
            followers = user_data.get('followers', 0)
            following = user_data.get('following', 0)
            public_repos = user_data.get('public_repos', 0)
            print(f"\n  User stats: 👥 {followers} followers | 👁️ {following} following | 📚 {public_repos} public repos")
    except:
        pass
    
    return {
        'total_stars': total_stars,
        'total_forks': total_forks,
        'total_watchers': total_watchers,
        'total_issues': total_issues,
        'repos': repos_found,
        'repo_count': len(repos_found),
        'languages': languages,
        'followers': followers
    }


def main():
    """Run all stats collection"""
    print("=" * 60)
    print("🚀 FETCHING ALL PACKAGE AND REPOSITORY STATISTICS")
    print("=" * 60)
    
    # Fetch all stats
    npm_stats = get_npm_stats()
    pypi_stats = get_pypi_stats()
    github_stats = get_github_stats()
    
    # Print summary
    print("\n" + "=" * 60)
    print("📊 SUMMARY STATISTICS")
    print("=" * 60)
    
    print("\n📦 NPM:")
    print(f"  Total packages: {npm_stats['package_count']}")
    print(f"  Total downloads (last year): {npm_stats['total_downloads']:,}")
    if npm_stats['packages']:
        print(f"  Packages: {', '.join(npm_stats['packages'][:10])}")
        if len(npm_stats['packages']) > 10:
            print(f"  ... and {len(npm_stats['packages']) - 10} more")
    
    print("\n🐍 PyPI:")
    print(f"  Total packages: {pypi_stats['package_count']}")
    if pypi_stats['total_downloads'] > 0:
        print(f"  Estimated annual downloads: {pypi_stats['total_downloads']:,}")
    if pypi_stats['packages']:
        print(f"  Packages: {', '.join(pypi_stats['packages'])}")
    
    print("\n🐙 GitHub:")
    print(f"  Total repositories: {github_stats['repo_count']}")
    print(f"  Total stars: {github_stats['total_stars']:,}")
    print(f"  Total forks: {github_stats['total_forks']:,}")
    print(f"  Total watchers: {github_stats['total_watchers']:,}")
    print(f"  Followers: {github_stats['followers']:,}")
    if github_stats['languages']:
        top_langs = sorted(github_stats['languages'].items(), key=lambda x: x[1], reverse=True)[:5]
        print(f"  Top languages: {', '.join(f'{lang}({count})' for lang, count in top_langs)}")
    
    print("\n🎯 GRAND TOTALS:")
    print(f"  Package downloads (NPM + PyPI): {npm_stats['total_downloads'] + pypi_stats['total_downloads']:,}")
    print(f"  Total packages/repos: {npm_stats['package_count'] + pypi_stats['package_count'] + github_stats['repo_count']}")
    print(f"  Community engagement (stars + forks): {github_stats['total_stars'] + github_stats['total_forks']:,}")
    
    # Save to JSON for later use
    all_stats = {
        'timestamp': datetime.now().isoformat(),
        'npm': npm_stats,
        'pypi': pypi_stats,
        'github': github_stats,
        'totals': {
            'downloads': npm_stats['total_downloads'] + pypi_stats['total_downloads'],
            'packages': npm_stats['package_count'] + pypi_stats['package_count'] + github_stats['repo_count'],
            'engagement': github_stats['total_stars'] + github_stats['total_forks']
        }
    }
    
    with open('portfolio_stats.json', 'w') as f:
        json.dump(all_stats, f, indent=2)
    print(f"\n💾 Stats saved to portfolio_stats.json")


if __name__ == "__main__":
    main()