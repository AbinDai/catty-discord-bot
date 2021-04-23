import discord, requests
from discord.ext import commands

class AnimalFacts(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.command()
    async def animalfacts(self, ctx, animalname=None):
        if not animalname:
            api = requests.get("https://cat-fact.herokuapp.com/facts/random?amount=1").json()
            type = api["type"]
            verified = api["status"]["verified"]
            text = api["text"]

            embed = discord.Embed(title="Animal Facts", color=ctx.guild.get_member(825761756252733531).color)
            embed.add_field(name="Type", value=type.capitalize())
            embed.add_field(name="Verified", value=verified)
            embed.add_field(
                name="⠀", 
                value="```\n"
                     f"{text}\n"
                      "```",
                inline=False
            )
            await ctx.send(embed=embed)
        else:
            try:
                api = requests.get(f"https://cat-fact.herokuapp.com/facts/random?animal_type={animalname}&amount=1").json()
                type = api["type"]
                verified = api["status"]["verified"]
                text = api["text"]

                embed = discord.Embed(title="Animal Facts", color=ctx.guild.get_member(825761756252733531).color)
                embed.add_field(name="Type", value=type.capitalize())
                embed.add_field(name="Verified", value=verified)
                embed.add_field(
                    name="⠀", 
                    value="```\n"
                        f"{text}\n"
                        "```",
                    inline=False
                )
                await ctx.send(embed=embed)
            except:
                embed = discord.Embed(description="❌ Nothing found", color=0xff0000)
                await ctx.reply(embed=embed, mention_author=False)

def setup(client):
    client.add_cog(AnimalFacts(client))