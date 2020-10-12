# tbbc_discord.py
import discord # https://discordpy.readthedocs.io/en/latest/faq.html
import tbbc_osu

# Constant strings
_token = ""
with open("discord_bot_token.txt","r") as f:
    _token = f.readline().strip()

mp_res_ch_id = 0 # ID of MP results channel
stat_ch_id = 0 # ID of statistics channel
with open("discord_channel_ids.txt","r") as f:
    mp_res_ch_id = int(f.readline().strip().split()[2])
    stat_ch_id = int(f.readline().strip().split()[2])

def not_negated(m_split_lower,i_word):
    if i_word == 0:
        return True
    if i_word >= 1: # "don't" or "no" (broken English)
        if m_split_lower[i_word-1] == "don't" or\
        m_split_lower[i_word-1] == "no":
            return False
    if i_word >= 2: # "do not"
        if m_split_lower[i_word-2] == "do" and\
        m_split_lower[i_word-1] == "not":
            return False
    return True

async def fetch_and_show(msg, m_split, m_split_lower, i_word):
    # General user info
    try:
        info = tbbc_osu.get_user(m_split[i_word+1])
    except IndexError:
        await msg.channel.send(":question: Not sure if I got you...")
    else:
        # Extract info
        username = info["username"]
        rank = info["pp_rank"]
        country = ""
        try:
            country = info["country"]
        except:
            return
        country_rank = info["pp_country_rank"]
        # Message info
        await msg.channel.send("User: {0}\n".format(username)
        + "Rank: #{0} (#{1} :flag_{2}:)".format(
        rank,country_rank,country.lower()))

class tbbc_discord_client(discord.Client):
    async def on_ready(self):
        print("Logged in as {0}".format(self.user))

    async def on_message(self,message):
        if message.author == self.user:
            return

        if message.channel.id == stat_ch_id:
            msg_split = message.content.split()
            msg_split_lower = message.content.lower().split()
            if "show" in msg_split_lower or "find" in msg_split_lower:
                try:
                    index = msg_split_lower.index("show")
                except ValueError:
                    index = msg_split_lower.index("find")
                finally:
                    if not_negated(msg_split_lower, index):
                        await fetch_and_show(message, msg_split,
                        msg_split_lower, index)

    def run(self):
        super().run(_token)
