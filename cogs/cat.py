import discord, requests
from discord.ext import commands

class Cat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["catimgs", "catimg", "catpics", "catpictures", "cat", "cats", "catimage"])
    async def catimages(self, ctx):
        api = requests.get("https://aws.random.cat/meow").json()
        picture = api["file"]

        embed = discord.Embed(
            title = "🐱 Meow",
            color = ctx.guild.get_member(825761756252733531).color
        )
        embed.set_image(url=picture)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Cat(client))