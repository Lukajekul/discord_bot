from discord.ext import commands
import discord

BAD_WORDS = ["badword1", "badword2", "badword3"]

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()

    async def kick(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("You need to mention someone to kick!")
            return

        if not ctx.guild.me.guild_permissions.kick_members:
            await ctx.send("I don't have permission to kick members!")
            return

        await member.kick(reason=f"Kicked by {ctx.author}")
        await ctx.send(f"{member.name} has been kicked by {ctx.author.name}.")

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

