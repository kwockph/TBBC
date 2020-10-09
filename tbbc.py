# tbbc.py
# Tournament bot by Coni

# Standard modules
import asyncio

# External modules

# Custom modules
from tbbc_discord import *
from tbbc_osu import *

async def main():
    print("=== TBBC ===")

    client = tbbc_discord_client()
    client.run()

asyncio.run(main())
