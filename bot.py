import os
import random
import discord, requests
from discord.ext import commands
intents= discord.Intents.all()
client = commands.Bot(command_prefix=">", intents=intents)
TOKEN = ""

@client.event
async def on_ready():
    print(client.user, "is online")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"TestBot-ProB1"))

@client.command()
async def read(ctx):
    print("test")
    headers = {
        "Host": "www.growtopia1.com",
        "User-Agent": "UbiServices_SDK_2019.Release.27_PC64_unicode_static"
    }
    data = 'version=4.04&platform=0&protocol=167'
    try:
        r = requests.post(f"https://www.growtopia1.com/growtopia/server_data.php", headers=headers, data=data)
        await ctx.send(f"```\n{r.text}```")
    except:
        await ctx.send("Can't connect to server")

client.run(TOKEN)
