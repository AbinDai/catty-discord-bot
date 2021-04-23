import discord, os #
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix=["c!", "C!"], case_insensitive=True)
client.remove_command("help")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

status = cycle(["c!help", "with some animals"])
@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_ready():
    change_status.start()
    print("bot siap!")

client.run(os.environ["DISCORD_TOKEN"])
