---
layout: project
title: "thrylen (VIVIFIED)"
description: "Encrypted messaging system with e-commerce cover for survivor safety"
repository: "https://github.com/DMontgomery40/thrylen"
tags: [JavaScript, Netlify, AES-256-GCM, Security, Cryptography]
category: security
featured: false
status: Active
last_updated: 2026-01-26
---

# thrylen (VIVIFIED Crystals)

**Encrypted Messaging with E-Commerce Cover**

A secure, encrypted messaging system disguised as legitimate e-commerce storefronts. Built for domestic violence survivors who need to communicate safely without detection. Zero footprint, zero traces.

---

## The Problem

Domestic violence survivors often cannot safely use standard messaging apps. Abusers may monitor phones, check message history, or recognize communication apps. VIVIFIED provides:

- **Plausible Deniability**: Looks like a shopping site
- **Zero Footprint**: No app install, no message history
- **Encrypted Communication**: AES-256-GCM end-to-end

---

## How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                    VIVIFIED Architecture                     │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Survivor visits "Crystals Shop" → Clicks specific product   │
│     ↓                                                         │
│  Product page has hidden message input (looks like review)   │
│     ↓                                                         │
│  Message encrypted with product-specific AES key             │
│     ↓                                                         │
│  Stored in Netlify Blobs (encrypted at rest)                 │
│     ↓                                                         │
│  Support contact visits "Shoes Shop" (different theme)       │
│     ↓                                                         │
│  Decrypts and reads message via their portal                 │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## Security Features

### Cryptography
- **AES-256-GCM**: Military-grade encryption
- **Per-Product Keys**: Each "product" has unique encryption key
- **IV Generation**: Fresh initialization vector per message
- **Key Derivation**: PBKDF2 with high iteration count

### Zero Footprint Design
- **No App Required**: Pure web, works in any browser
- **No Local Storage**: Nothing saved to device
- **Generic Errors**: "Product unavailable" instead of "auth failed"
- **No Comments in Code**: Obfuscated production build

### Access Control
- **HTTPOnly Cookies**: Prevents XSS token theft
- **Secure + SameSite**: CSRF protection
- **Rate Limiting**: Brute force prevention
- **Session Timeout**: Auto-logout after inactivity

---

## Multi-Theme Architecture

The system supports 30+ different storefront themes:

| Theme | Cover Story |
|-------|-------------|
| Crystals | Healing crystals shop |
| Shoes | Footwear boutique |
| Candles | Home fragrance store |
| Plants | Nursery/garden shop |
| Books | Used bookstore |

Each theme is a complete, functional-looking e-commerce site.

---

## Tech Stack

- **Frontend**: Vanilla JavaScript (no frameworks = smaller footprint)
- **Backend**: Netlify Functions (serverless)
- **Storage**: Netlify Blobs (encrypted)
- **Crypto**: Web Crypto API (native browser)
- **Deployment**: Netlify (free tier works)

---

## Why Vanilla JS?

No React, no Vue, no build tools visible in network tab. The site looks exactly like a simple Shopify store. Framework fingerprints could reveal it's not a real store.

---

## Privacy Considerations

This project is open-sourced with careful consideration:

- **No Real Deployments Listed**: URLs not published
- **Generic Documentation**: Doesn't reveal partner organizations
- **Security Through Openness**: Crypto is auditable

---

## Links

- [GitHub Repository](https://github.com/DMontgomery40/thrylen)
