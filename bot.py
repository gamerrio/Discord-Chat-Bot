import discord, os
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = str(os.getenv("TOKEN"))

Cogs = [
    "general",
    'jishaku'
]
class Bot(commands.Bot):
    def __init__(self):
        # initialize our bot instance, make sure to pass your intents!
        # for this example, we'll just have everything enabled
        super().__init__(
            command_prefix="!",
             intents=discord.Intents.all()
        )


# the method to override in order to run whatever you need before your bot starts
    async def setup_hook(self):
        for ext in Cogs:
            await self.load_extension(ext)
            print("Loaded extension: " + ext)

Bot().run(TOKEN)