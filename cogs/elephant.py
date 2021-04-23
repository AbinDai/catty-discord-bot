import discord, requests, random
from discord.ext import commands

class Elephant(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(aliases=["elephants"], invoke_without_command=True)
    async def elephant(self, ctx):
        embed = discord.Embed(
            title = "Command Usage",
            description = "`c!elephant random` to return a random elephants.\n" #done
                          "`c!elephant sex [male/female]` to return an elephant list with their sex.\n" #done
                          "`c!elephant name [their name]` to return an elephant with their name.\n", #done
            color = ctx.guild.get_member(825761756252733531).color
        )
        embed.set_footer(text="Remember to not including the brackets while doing these stuffs.")
        await ctx.send(embed=embed)

    @elephant.command()
    async def random(self, ctx):
        try:
            api = requests.get("https://elephant-api.herokuapp.com/elephants/random").json()
            name = api[0]["name"]
            affiliation = api[0]["affiliation"]
            species = api[0]["species"]
            sex = api[0]["sex"]
            dob = api[0]["dob"]
            dod = api[0]["dod"]
            wikilink = api[0]["wikilink"]
            image = api[0]["image"]
            note = api[0]["note"]

            embed = discord.Embed(title="Random Elephants", color=ctx.guild.get_member(825761756252733531).color)
            embed.set_thumbnail(url=image)
            embed.add_field(name="Name", value=f"[{name}]({wikilink})")
            embed.add_field(name="Affiliation", value=affiliation)
            embed.add_field(name="Species", value=species)
            embed.add_field(name="Sex", value=sex)
            embed.add_field(name="Birth Date", value=dob)
            embed.add_field(name="Death Date", value=dod)
            embed.add_field(name="⠀", value=f"```\n{note}\n```", inline=False)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(description="❌ Failed while making request. Try again later.", color=0xff0000)
            await ctx.reply(embed=embed, mention_author=False)

    @elephant.command(aliases=["gender"])
    async def sex(self, ctx, sex):
        try:
            if sex == "male":
                api = requests.get(f"https://elephant-api.herokuapp.com/elephants/sex/{sex}?amount=10").json()
                oneName = api[0]["name"]
                oneLink = api[0]["wikilink"]
                firstImage = api[0]["image"]

                twoName = api[1]["name"]
                twoLink = api[1]["wikilink"]
                twoImage = api[1]["image"]

                threeName = api[2]["name"]
                threeLink = api[2]["wikilink"]
                threeimage = api[2]["image"]

                fourName = api[3]["name"]
                fourLink = api[3]["wikilink"]
                fourImage = api[3]["image"]

                fiveName = api[4]["name"]
                fiveLink = api[4]["wikilink"]
                fiveImage = api[4]["image"]

                sixName = api[5]["name"]
                sixLink = api[5]["wikilink"]
                sixImage = api[5]["image"]

                sevenName = api[6]["name"]
                sevenLink = api[6]["wikilink"]
                sevenImage = api[6]["image"]

                eightName = api[7]["name"]
                eightLink = api[7]["wikilink"]
                eightImage = api[7]["image"]

                nineName = api[8]["name"]
                nineLink = api[8]["wikilink"]
                nineImage = api[8]["image"]

                tenName = api[9]["name"]
                tenLink = api[9]["wikilink"]
                tenImage = api[9]["image"]

                random_images = [
                    f"{firstImage}",
                    f"{twoImage}",
                    f"{threeimage}",
                    f"{fourImage}",
                    f"{fiveImage}",
                    f"{sixImage}",
                    f"{sevenImage}",
                    f"{eightImage}",
                    f"{nineImage}",
                    f"{tenImage}"
                ]

                embed = discord.Embed(
                    title = "Male Elephants",
                    description = f"1. [{oneName}]({oneLink})\n"
                                f"2. [{twoName}]({twoLink})\n"
                                f"3. [{threeName}]({threeLink})\n"
                                f"4. [{fourName}]({fourLink})\n"
                                f"5. [{fiveName}]({fiveLink})\n"
                                f"6. [{sixName}]({sixLink})\n"
                                f"7. [{sevenName}]({sevenLink})\n"
                                f"8. [{eightName}]({eightLink})\n"
                                f"9. [{nineName}]({nineLink})\n"
                                f"10. [{tenName}]({tenLink})\n",
                    color = ctx.guild.get_member(825761756252733531).color
                )
                embed.set_thumbnail(url=random.choice(random_images))
                embed.set_footer(text="And more...")
                await ctx.send(embed=embed)
            elif sex == "female":
                api = requests.get(f"https://elephant-api.herokuapp.com/elephants/sex/{sex}?amount=10").json()
                oneName = api[0]["name"]
                oneLink = api[0]["wikilink"]
                firstImage = api[0]["image"]

                twoName = api[1]["name"]
                twoLink = api[1]["wikilink"]
                twoImage = api[1]["image"]

                threeName = api[2]["name"]
                threeLink = api[2]["wikilink"]
                threeimage = api[2]["image"]

                fourName = api[3]["name"]
                fourLink = api[3]["wikilink"]
                fourImage = api[3]["image"]

                fiveName = api[4]["name"]
                fiveLink = api[4]["wikilink"]
                fiveImage = api[4]["image"]

                sixName = api[5]["name"]
                sixLink = api[5]["wikilink"]
                sixImage = api[5]["image"]

                sevenName = api[6]["name"]
                sevenLink = api[6]["wikilink"]
                sevenImage = api[6]["image"]

                eightName = api[7]["name"]
                eightLink = api[7]["wikilink"]
                eightImage = api[7]["image"]

                nineName = api[8]["name"]
                nineLink = api[8]["wikilink"]
                nineImage = api[8]["image"]

                tenName = api[9]["name"]
                tenLink = api[9]["wikilink"]
                tenImage = api[9]["image"]

                random_images = [
                    f"{firstImage}",
                    f"{twoImage}",
                    f"{threeimage}",
                    f"{fourImage}",
                    f"{fiveImage}",
                    f"{sixImage}",
                    f"{sevenImage}",
                    f"{eightImage}",
                    f"{nineImage}",
                    f"{tenImage}"
                ]

                embed = discord.Embed(
                    title = "Female Elephants",
                    description = f"1. [{oneName}]({oneLink})\n"
                                f"2. [{twoName}]({twoLink})\n"
                                f"3. [{threeName}]({threeLink})\n"
                                f"4. [{fourName}]({fourLink})\n"
                                f"5. [{fiveName}]({fiveLink})\n"
                                f"6. [{sixName}]({sixLink})\n"
                                f"7. [{sevenName}]({sevenLink})\n"
                                f"8. [{eightName}]({eightLink})\n"
                                f"9. [{nineName}]({nineLink})\n"
                                f"10. [{tenName}]({tenLink})\n",
                    color = ctx.guild.get_member(825761756252733531).color
                )
                embed.set_thumbnail(url=random.choice(random_images))
                embed.set_footer(text="And more...")
                await ctx.send(embed=embed)
        except:
            embed = discord.Embed(description="❌ Only **male** and **female** genders allowed!", color=0xff0000)
            await ctx.reply(embed=embed, mention_author=False)
    @sex.error
    async def on_sex_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("❌ You must include the gender!\nExample: `c!elephant sex [male/female]`", mention_author=False)

    @elephant.command()
    async def name(self, ctx, *name):
        try:
            their_name = "%20".join(name)
            api = requests.get(f"https://elephant-api.herokuapp.com/elephants/name/{their_name}").json()
            name = api["name"]
            affiliation = api["affiliation"]
            species = api["species"]
            sex = api["sex"]
            dob = api["dob"]
            dod = api["dod"]
            wikilink = api["wikilink"]
            image = api["image"]
            note = api["note"]

            embed = discord.Embed(title=f'The "{name}" Elephant', color=ctx.guild.get_member(825761756252733531).color)
            embed.set_thumbnail(url=image)
            embed.add_field(name="Name", value=f"[{name}]({wikilink})")
            embed.add_field(name="Affiliation", value=affiliation)
            embed.add_field(name="Species", value=species)
            embed.add_field(name="Sex", value=sex)
            embed.add_field(name="Birth Date", value=dob)
            embed.add_field(name="Death Date", value=dod)
            embed.add_field(name="⠀", value=f"```\n{note}\n```", inline=False)
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(description="❌ Nothing found\nDon't forget to include the name! (It's case sensitive).", color=0xff0000)
            await ctx.reply(embed=embed, mention_author=False)
    @name.error
    async def on_name_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("❌ You must include the name!\nExample: `c!elephant name Ziggy` (it's case sensitive btw).", mention_author=False)



def setup(client):
    client.add_cog(Elephant(client))