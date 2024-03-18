import os
from typing import Final
from dotenv import load_dotenv
from discord import Intents, Client, Interaction
from discord.ext import commands
from discord_slash  import SlashCommand, SlashContext

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=intents)

    async def on_ready(self):
        print(f'{self.user} is now running!')

client = MyBot()
slash = SlashCommand(client, sync_commands=True)

@slash.slash(name="hello_world", description="Prints Hello World")
async def _hello_world(ctx: SlashContext):
    await ctx.send(content="Hello World")

if __name__ == '__main__':
    client.run(TOKEN)