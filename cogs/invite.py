import discord
from discord.ext import commands

class Invite(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["inv"])
    async def invite(self, ctx):
        embed = discord.Embed(
            title = "You Want Me on Your Server?",
            description = "[Here's](https://discord.com/api/oauth2/authorize?client_id=825761756252733531&permissions=84992&scope=bot) my invite link.",
            color = ctx.guild.get_member(825761756252733531).color
        )
        embed.set_thumbnail(url=self.client.user.avatar_url_as(format="png", size=4096))
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Invite(client))