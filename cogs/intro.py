import discord
from discord.ext import commands

class Intro(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                embed = discord.Embed(
                    title = "Thanks for inviting me 😁",
                    description = "Just a quick review. My name is Catty and my prefix is `c!`. I'm a bot that talks about animals.\nTo get started, type `c!help` to see my available commands.\nTo see a detailed info about a command, use `c!help [command name]`.\nTo execute a command, use `c![command name]`.\nThank you, and have a nice day!",
                    color = 0xe9cd50
                )
                embed.set_thumbnail(url=self.client.user.avatar_url)
                await channel.send(embed=embed)
            break

def setup(client):
    client.add_cog(Intro(client))