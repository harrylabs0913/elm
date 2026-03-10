# Eleme (饿了么) Skill

CLI tool for Eleme food delivery platform.

## Commands

### Search Food/Restaurants
```bash
elm search "奶茶"
elm search "汉堡" --location "北京市朝阳区" --limit 20
```

### Login
```bash
elm login
```
Opens browser with QR code for authentication.

### Red Packet Info
```bash
elm redpacket
```
Shows available coupons and red packets.

## Features

- Restaurant search with caching
- QR code login
- Coupon/red packet tracking
- Delivery time and fee info
- Rating and sales data
- Anti-detection browser automation

## Dependencies

Requires `ecommerce-core` framework.

## Data Storage

- Sessions: `~/.openclaw/data/ecommerce/auth.db`
- Cache: `~/.openclaw/data/ecommerce/ecommerce.db`
