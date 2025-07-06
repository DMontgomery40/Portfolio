source "https://rubygems.org"

# Use GitHub Pages gem (includes Jekyll and all compatible plugins)
gem "github-pages", group: :jekyll_plugins

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]

# For development and testing
group :development, :test do
  gem "html-proofer", "~> 3.19"
  gem "rake"
end