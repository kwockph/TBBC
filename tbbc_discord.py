# tbbc_discord.py
import discord # https://discordpy.readthedocs.io/en/latest/faq.html

# Constant strings
_token = ""
with open("discord_bot_token.txt","r") as f:
    _token = f.readline().strip()

mp_res_ch_id = "" # ID of MP results channel
stat_ch_id = "" # ID of statistics channel
with open("discord_channel_ids.txt","r") as f:
    mp_res_ch_id = f.readline().strip().split()[2]
    stat_ch_id = f.readline().strip().split()[2]

class tbbc_discord_client(discord.Client):
    async def on_ready(self):
        print("Logged in as {0}".format(self.user))

    async def on_message(self,message):
        if message.author == self.user:
            return
        if message.content.startswith("$hello"):
            await message.channel.send("Hello!")

    def run(self):
        super().run(_token)
