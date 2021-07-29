import discord
from discord.ext import commands

import os

TOKEN = os.environ.get("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="?", intents=intents)
RoomID = os.environ.get("ROOMID")


@bot.event
async def on_ready():
    print("ログインしました")


@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        embed = discord.Embed(
            title="入室通知",
            color=0x00ff00,
            description="<#" + str(after.channel.id) + ">に<@!" + str(member.id) + ">が参加しました。"
        )
        embed.set_footer(text="Made by のぶ, ばにあ")

        if after.channel is not None:
            await bot.get_channel(RoomID).send(embed=embed)


if __name__ == "__main__":
    bot.run(TOKEN)
