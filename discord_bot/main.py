import discord
bot=discord.Bot()

@bot.event
async def on_ready():
    print("logged in as {bot.user}.")

testingservers=[insert your testserver client]

@bot.slash_command(guide_ids=testingservers,name="work",description="checks to see if user online")
async def work(ctx):
    await ctx.respond(f"I am working! \n\nLatency: {bot.latency*1000} ms.")

bot.run('insert your token')
