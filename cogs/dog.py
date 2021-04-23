import discord, requests
from discord.ext import commands

class Dog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["dogimgs", "dogimg", "dog", "dogs", "dogpicture", "dogpictures", "dogpic", "dogpics"])
    async def dogimages(self, ctx):
        api = requests.get("https://random.dog/woof.json?ref=apilist.fun").json()
        picture = api["url"]

        embed = discord.Embed(
            title = "🐶 Woof-Woof",
            color = ctx.guild.get_member(825761756252733531).color
        )
        embed.set_image(url=picture)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Dog(client))