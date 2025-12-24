from discord.ext import commands

BAD_WORDS = ["badword1", "badword2", "badword3"]

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def kick(self, ctx):
        await ctx.send("Kick command works")


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        content = message.content.lower()

        for word in BAD_WORDS:
            if word in content:
                await message.delete()
                await message.channel.send(
                    f"{message.author.mention} watch your language."
                )
                break

        await self.bot.process_commands(message)

