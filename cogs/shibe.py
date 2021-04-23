import discord, requests
from discord.ext import commands

class ShibeDog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["shibe"])
    async def shibedog(self, ctx):
        api = requests.get("http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true").json()
        image = api[0]

        embed = discord.Embed(title="🐕 Shibe Dog", color=ctx.guild.get_member(825761756252733531).color)
        embed.set_image(url=image)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(ShibeDog(client))