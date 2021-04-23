import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def ping(self, ctx):
        ping = round(self.client.latency*1000)

        if ping <= 299:
            embed = discord.Embed(
                description = f"📶 {ping}ms",
                color = discord.Color.green()
            )
            await ctx.send(embed=embed)
        elif ping >= 300 and ping <= 399:
            embed = discord.Embed(
                description = f"📶 {ping}ms",
                color = discord.Color.gold()
            )
            await ctx.send(embed=embed)
        elif ping >= 400:
            embed = discord.Embed(
                description = f"📶 {ping}ms",
                color = discord.Color.red()
            )
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Ping(client))