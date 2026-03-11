---
name: Eleme Food Delivery
slug: elm
version: 1.1.0
homepage: https://clawic.com/skills/elm
description: Navigate Eleme (饿了么) food delivery with smart restaurant selection, deal finding, and ordering strategies.
metadata:
  clawdbot:
    emoji: "🍜"
    requires:
      bins: []
    os: ["linux", "darwin", "win32"]
---

## When to Use

User wants to order food delivery via Eleme (饿了么). Agent helps with restaurant discovery, deal optimization, red packet strategies, and navigating China's leading food delivery platform.

## Quick Reference

| Topic | File |
|-------|------|
| Restaurant vetting | `restaurants.md` |
| Deal optimization | `deals.md` |
| Red packet strategy | `redpackets.md` |

## Core Rules

### 1. Platform Overview: Eleme vs Meituan

| Platform | Strengths | Best For |
|----------|-----------|----------|
| **Eleme (饿了么)** | Alibaba ecosystem, better for chain restaurants | Consistent quality, corporate accounts |
| **Meituan (美团)** | More local options, aggressive pricing | Variety, local favorites, better deals |

**Strategy:** Check both platforms for the same restaurant - prices and promotions often differ.

### 2. Restaurant Selection Protocol

**Rating System Decoded:**

| Rating | Meaning | Action |
|--------|---------|--------|
| 4.8+ | Excellent | Safe choice |
| 4.5-4.7 | Good | Check recent reviews |
| 4.0-4.4 | Average | Read reviews carefully |
| <4.0 | Poor | Avoid unless desperate |

**Key Metrics to Check:**
- **月销量** (Monthly sales) - Higher is better
- **配送时间** (Delivery time) - Under 45min ideal
- **起送价** (Minimum order) - Factor into total cost
- **配送费** (Delivery fee) - Some restaurants waive this

**Red Flags:**
- No photos in reviews
- Recent complaints about food safety
- Delivery time consistently >60 minutes
- Low sales volume (<100/month)

### 3. Deal Optimization Strategy

**Red Packet (红包) Hierarchy:**

| Type | Typical Value | How to Get |
|------|---------------|------------|
| 平台红包 | ¥3-10 | Daily check-in, promotions |
| 店铺红包 | ¥2-15 | Restaurant-specific |
| 会员红包 | ¥5-20 | Super Member subscription |
| 银行优惠 | ¥5-30 | Credit card partnerships |

**Stacking Strategy:**
1. Collect all available red packets first
2. Check "满减" (spend-and-save) restaurant offers
3. Combine: 店铺红包 + 平台红包 + 银行卡优惠
4. Order during "蜂鸟专送" promotions for free delivery

**Best Ordering Times:**
- 10:30-11:00 AM - Pre-lunch, less rush
- 2:00-4:00 PM - Afternoon tea deals
- 8:00-9:00 PM - Dinner off-peak
- Avoid 11:30-1:00 PM and 6:00-7:30 PM (long waits)

### 4. Super Member (超级会员) Analysis

**Cost:** ~¥10-15/month

**Benefits:**
- 4-6 red packets monthly (¥5-10 each)
- Free delivery on many orders
- Exclusive member prices
- Priority customer service

**Worth It If:**
- You order >4 times/month
- Average order >¥30
- You use Eleme regularly (not just occasionally)

### 5. Food Safety & Quality

**Check Before Ordering:**

| Indicator | Good Sign | Bad Sign |
|-----------|-----------|----------|
| **商家资质** | 明厨亮灶 (open kitchen) | No photos of kitchen |
| **食品安全等级** | A or B grade | C grade or no display |
| **Review photos** | Consistent with menu | Look very different |
| **Recent reviews** | Positive trend | Declining quality |

**High-Risk Foods to Avoid:**
- Raw/undercooked items from unknown vendors
- Sushi from non-specialized restaurants
- Salads in summer (delivery time risk)

### 6. Order Optimization

**Cart Building Strategy:**

1. **Meet minimum order** efficiently
   - Add small items (饮料, 小菜) to hit threshold
   - Don't overspend just to get free delivery

2. **Group ordering**
   - Split delivery fee with colleagues/friends
   - Check "多人拼单" (group order) options

3. **Timing tricks**
   - Pre-order for specific delivery time
   - "准时达" (on-time delivery) guarantee for important meals

4. **Special requests**
   - Use "备注" (notes) for dietary restrictions
   - Request less oil/spicy: "少油少辣"
   - Allergies: "不要XX" (no XX)

### 7. Delivery & Post-Order

**Tracking Your Order:**
- 已接单 (Order received)
- 商家备餐中 (Preparing)
- 骑手已取餐 (Picked up)
- 配送中 (Delivering)
- 已送达 (Delivered)

**When Things Go Wrong:**

| Issue | Solution |
|-------|----------|
| Wrong order | Contact rider immediately, photo evidence |
| Cold food | Request re-delivery or partial refund |
| Missing items | Report via app, usually quick resolution |
| Late delivery | Check if eligible for "准时达" compensation |
| Quality issues | Rate honestly, affects restaurant ranking |

**Refund Policy:**
- Food issues: Full refund usually granted
- Wrong delivery: Exchange or refund
- Change of mind: Only before restaurant accepts

## Common Traps

- **Ignoring delivery distance** → Cold food, long wait
- **Ordering during peak hours** → 60+ min waits
- **Not checking red packets first** → Leaving money on table
- **Blindly trusting ratings** → Fake reviews exist
- **Forgetting dietary notes** → Wrong preparation
- **Not comparing with Meituan** → Better deals elsewhere
- **Ordering from new/untested restaurants** → Quality gamble

## Platform Features to Leverage

### Eleme Specific
- **饿了么果园** - Gamified discounts through "farming"
- **吃货豆** - Loyalty points for orders
- **品牌联盟** - Chain restaurant discounts
- **企业订餐** - Corporate account benefits

### Payment Optimization
- **支付宝** - Often has exclusive Eleme coupons
- **花呗** - Occasional installment deals for large orders
- **信用卡** - Bank partnerships for extra discounts

## Related Skills

Install with `clawhub install <slug>` if user confirms:
- `meituan` - Meituan food delivery guidance
- `shopping` - General shopping assistance
- `alibaba-shopping` - Taobao/Tmall shopping guide

## Feedback

- If useful: `clawhub star elm`
- Stay updated: `clawhub sync`
