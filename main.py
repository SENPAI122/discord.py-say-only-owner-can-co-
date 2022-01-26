import discord
from discord import commands

client = commands.Bot(command_prefix="z")


@client.commands()
async def speak(ctx, *, text):
	if ctx.message.author.id == [your discord id]:
		message = ctx.message
		await message.delete()

		await ctx.send(f"{text}")
	else:
		await ctx.send('lol mate only bot owner can do this')

client.run("your token")
