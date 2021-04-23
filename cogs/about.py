import discord
from discord.ext import commands

class About(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["info", "botinfo", "botstats", "stats"])
    async def about(self, ctx):
        embed = discord.Embed(
            title = "About this Bot",
            description = "```\n"
                          "Bot's name     : Catty#0755\n"
                          "Prefix         : c!\n"
                          "Developed by   : Abin#4405\n"
                          "Creation date⠀ : Mar 29, 2021\n"
                          f"Used in⠀⠀⠀  ⠀⠀: {len(self.client.guilds)} servers\n"
                          "Library⠀⠀⠀⠀  ⠀: discord.py\n"
                          f"Library version: {discord.__version__}\n"
                          f"Bot's latency  : {round(self.client.latency*1000)}ms\n"
                          "GitHub Repo     : https://github.com/AbinDai/catty-discord-bot"
                          "```",
            color = ctx.guild.get_member(825761756252733531).color
        )
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(About(client))
