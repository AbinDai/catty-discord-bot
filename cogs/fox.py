import discord, requests
from discord.ext import commands

class Fox(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["foximgs", "foximg", "fox", "foxes", "foxpictures", "foximage", "foxpicture", "foxpic"])
    async def foximages(self, ctx):
        api = requests.get("https://randomfox.ca/floof/").json()
        image = api["image"]

        embed = discord.Embed(title="🦊 Fox", color=ctx.guild.get_member(825761756252733531).color)
        embed.set_image(url=image)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fox(client))