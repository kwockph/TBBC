# tbbc.py
# Tournament bot by Coni

# Standard modules
import asyncio
#import nest_asyncio
#nest_asyncio.apply()

# External modules

# Custom modules
from tbbc_discord import *
from tbbc_osu import *

def main():
    print("=== TBBC ===")

    client = tbbc_discord_client()
    client.run()

asyncio.run(main())
