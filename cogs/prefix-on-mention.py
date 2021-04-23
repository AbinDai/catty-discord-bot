import discord
from discord.ext import commands

class Prefix(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.client.user.mentioned_in(message):
            await message.channel.send(f'Hi {message.author.name}! My prefix is `c!`.')

def setup(client):
    client.add_cog(Prefix(client))