#!/usr/bin/env python3
"""
Eleme (饿了么) CLI Tool
"""

import asyncio
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from adapter import ElemeAdapter


async def search_command(args):
    """Search food/restaurants"""
    adapter = ElemeAdapter(headless=args.headless)
    
    try:
        results = await adapter.search(args.keyword, location=args.location)
        
        print(f"\nFound {len(results)} restaurants for '{args.keyword}':\n")
        
        for i, restaurant in enumerate(results[:args.limit], 1):
            print(f"{i}. {restaurant.get('name', 'N/A')}")
            print(f"   Rating: {restaurant.get('rating', 'N/A')}")
            print(f"   Monthly Sales: {restaurant.get('month_sales', 'N/A')}")
            print(f"   Delivery: {restaurant.get('delivery_time', 'N/A')}")
            print(f"   Delivery Fee: ¥{restaurant.get('delivery_fee', 'N/A')}")
            print(f"   Min Order: ¥{restaurant.get('min_order', 'N/A')}")
            if restaurant.get('tags'):
                print(f"   Tags: {', '.join(restaurant['tags'])}")
            print(f"   URL: {restaurant.get('url', 'N/A')}")
            print()
            
    finally:
        await adapter.close()


async def login_command(args):
    """Login with QR code"""
    adapter = ElemeAdapter(headless=False)
    
    try:
        print("Initializing browser...")
        await adapter.init()
        
        print("Getting QR code...")
        qr_code = await adapter.login_qr()
        
        if qr_code:
            print(f"\nQR Code URL: {qr_code[:100]}...")
            print("\nPlease scan the QR code with Eleme app to login.")
            print("Waiting for login (timeout: 120s)...")
            
            await asyncio.sleep(120)
        else:
            print("Failed to get QR code")
            
    finally:
        await adapter.close()


async def redpacket_command(args):
    """Get red packet/coupon info"""
    adapter = ElemeAdapter(headless=args.headless)
    
    try:
        info = await adapter.get_redpacket_info()
        
        if info:
            print(f"\nCoupon Info:")
            print(f"  Total Coupons: {info.get('coupon_count', 0)}")
            
            coupons = info.get('coupons', [])
            if coupons:
                print(f"\n  Your Coupons:")
                for coupon in coupons:
                    print(f"    - ¥{coupon['amount']} {coupon.get('type', '')}")
                    print(f"      Condition: {coupon.get('condition', 'N/A')}")
                    print(f"      Valid Until: {coupon.get('valid_until', 'N/A')}")
        else:
            print("Failed to get coupon info")
            
    finally:
        await adapter.close()


def main():
    parser = argparse.ArgumentParser(description='Eleme CLI Tool')
    parser.add_argument('--headless', action='store_true', help='Run in headless mode')
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Search food/restaurants')
    search_parser.add_argument('keyword', help='Search keyword (e.g., 奶茶, 汉堡)')
    search_parser.add_argument('--location', help='Delivery address')
    search_parser.add_argument('--limit', type=int, default=10, help='Result limit')
    
    # Login command
    login_parser = subparsers.add_parser('login', help='Login with QR code')
    
    # Redpacket command
    redpacket_parser = subparsers.add_parser('redpacket', help='Get red packet info')
    
    args = parser.parse_args()
    
    if args.command == 'search':
        asyncio.run(search_command(args))
    elif args.command == 'login':
        asyncio.run(login_command(args))
    elif args.command == 'redpacket':
        asyncio.run(redpacket_command(args))
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
