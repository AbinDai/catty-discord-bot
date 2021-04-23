import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True, aliases=["h"])
    async def help(self, ctx):
        embed = discord.Embed(
            title = "Catty Bot Command List",
            description = "Hi, I'm Catty! A Discord bot that has an animal based commands.\n"
                          "Use `c!help [command name]` to see an info about a command.\n"
                          "I also have a GitHub repo! [Heres](https://github.com/AbinDai/catty-discord-bot/) the link."
                          "⠀\n"
                          "**Main Commands**\n"
                          "`c!catimages`\n"
                          "Shows some random cat images.\n"
                          "⠀\n"
                          "`c!dogimages`\n"
                          "Shows some random dog images.\n"
                          "⠀\n"
                          "`c!foximages`\n"
                          "Shows some random fox images\n"
                          "⠀\n"
                          "`c!shibedog`\n"
                          "Shows some random Shibe Inu pictures.\n"
                          "⠀\n"
                          "`c!animalfacts`\n"
                          "Shows some random animal facts.\n"
                          "⠀\n"
                          "`c!elephant`\n"
                          "Shows an elephant info and detail.\n"
                          "⠀\n"
                          "**Miscellaneous Commands**\n"
                          "`c!ping`\n"
                          "Shows the bot's latency.\n"
                          "⠀\n"
                          "`c!invite`\n"
                          "Gives you my invite link.\n"
                          "⠀\n"
                          "`c!about`\n"
                          "Shows the bot's info.\n"
                          "⠀\n"
                          "`c!help`\n"
                          "Shows this panel.",
            color = ctx.guild.get_member(825761756252733531).color
        )
        embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.send(embed=embed)


###################################################################################################################


    @help.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            description = "Shows the bot's latency.",
            color = ctx.guild.get_member(825761756252733531).color
        )
        embed.set_author(name="Help > Ping", icon_url=self.client.user.avatar_url)
        embed.add_field(name="Category", value="Miscellaneous")
        embed.add_field(name="Aliases", value=None)
        embed.add_field(name="Usage", value="`c!ping`")
        await ctx.send(embed=embed)

    @help.command(aliases=["inv"])
    async def invite(self, ctx):
        embed = discord.Embed(
            description = "Gives you my invite link.",
            color = ctx.guild.get_member(825761756252733531).color
        )
        embed.set_author(name="Help > Invite", icon_url=self.client.user.avatar_url)
        embed.add_field(name="Category", value="Miscellaneous")
        embed.add_field(name="Aliases", value="`inv`")
        embed.add_field(name="Usage", value="`c!invite`")
        await ctx.send(embed=embed)

    @help.command(aliases=["info", "botinfo", "botstats", "stats"])
    async def about(self, ctx):
        embed = discord.Embed(
            description = "Shows the bots info.",
            color = ctx.guild.get_member(825761756252733531).color
        )
        embed.set_author(name="Help > About", icon_url=self.client.user.avatar_url)
        embed.add_field(name="Category", value="Miscellaneous")
        embed.add_field(name="Aliases", value="`info`\n`botinfo`\n`botstats`\n`stats`")
        embed.add_field(name="Usage", value="`c!about`")
        await ctx.send(embed=embed)

    @help.command(name="help", aliases=["h"])
    async def _help(self, ctx):
        embed = discord.Embed(
            description = "Shows the bot's command list and some infos.",
            color = ctx.guild.get_member(825761756252733531).color
        )
        embed.set_author(name="Help > Help", icon_url=self.client.user.avatar_url)
        embed.add_field(name="Category", value="Miscellaneous")
        embed.add_field(name="Aliases", value="`h`")
        embed.add_field(name="Usage", value="`c!help`")
        await ctx.send(embed=embed)

    @help.command(aliases=["catimgs", "catimg", "catpics", "catpictures", "cat", "cats", "catimage"])
    async def catimages(self, ctx):
        embed = discord.Embed(
            description = "Shows some random cat images.",
            color = ctx.guild.get_member(825761756252733531).color
        )
        embed.set_author(name="Help > CatImages", icon_url=self.client.user.avatar_url)
        embed.add_field(name="Category", value="Main")
        embed.add_field(name="Aliases", value="`catimgs`\n`catimg`\n`catpics`\n`catpictures`\n`cat`\n`cats`\n`catimage`")
        embed.add_field(name="Usage", value="`c!catimages`")
        await ctx.send(embed=embed)

    @help.command(aliases=["dogimgs", "dogimg", "dog", "dogs", "dogpicture", "dogpictures", "dogpic", "dogpics"])
    async def dogimages(self, ctx):
        embed = discord.Embed(
            description = "Shows some random dog images.",
            color = ctx.guild.get_member(825761756252733531).color
        )
        embed.set_author(name="Help > DogImages", icon_url=self.client.user.avatar_url)
        embed.add_field(name="Category", value="Main")
        embed.add_field(name="Aliases", value="`dogimgs`\n`dogimg`\n`dog`\n`dogs`\n`dogpicture`\n`dogpictures`\n`dogpic`\n`dogpics`")
        embed.add_field(name="Usage", value="`c!dogimages`")
        await ctx.send(embed=embed)

    @help.command(aliases=["foximgs", "foximg", "fox", "foxes", "foxpictures", "foximage", "foxpicture", "foxpic"])
    async def foximages(self, ctx):
        embed = discord.Embed(
            description = "Shows some random fox images.",
            color = ctx.guild.get_member(825761756252733531).color
        )
        embed.set_author(name="Help > FoxImages", icon_url=self.client.user.avatar_url)
        embed.add_field(name="Category", value="Main")
        embed.add_field(name="Aliases", value="`foximgs`\n`foximg`\n`fox`\n`foxes`\n`foxpictures`\n`foximage`\n`foxpicture`\n`foxpic`")
        embed.add_field(name="Usage", value="`c!foximages`")
        await ctx.send(embed=embed)

    @help.command(aliases=["shibe"])
    async def shibedog(self, ctx):
        embed = discord.Embed(
            description = "Shows some random Shibe dog images.",
            color = ctx.guild.get_member(825761756252733531).color
        )
        embed.set_author(name="Help > ShibeDog", icon_url=self.client.user.avatar_url)
        embed.add_field(name="Category", value="Main")
        embed.add_field(name="Aliases", value="`shibe`")
        embed.add_field(name="Usage", value="`c!shibedog`")
        await ctx.send(embed=embed)

    @help.command()
    async def animalfacts(self, ctx):
        embed = discord.Embed(
            description = "Shows some random animal facts. (Leave without additional argument to return a random cat facts).",
            color = ctx.guild.get_member(825761756252733531).color
        )
        embed.set_author(name="Help > AnimalFacts", icon_url=self.client.user.avatar_url)
        embed.add_field(name="Category", value="Main")
        embed.add_field(name="Aliases", value=None)
        embed.add_field(name="Usage", value="`c!animalfacts`\n`c!animalfacts [animal name]`")
        await ctx.send(embed=embed)

    @help.command(aliases=["elephants"])
    async def elephant(self, ctx):
        embed = discord.Embed(
            description = "Shows some elephant details.",
            color = ctx.guild.get_member(825761756252733531).color
        )
        embed.set_author(name="Help > Elephant", icon_url=self.client.user.avatar_url)
        embed.add_field(name="Category", value="Main")
        embed.add_field(name="Aliases", value="`elephants`")
        embed.add_field(name="Usage", value="`c!elephant random`\n`c!elephant sex [male/female]`\n`c!elephant name [their name]`")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))
