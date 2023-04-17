from discord import app_commands
from discord.ext import commands
import discord,os
from dotenv import load_dotenv
from pyllamacpp.model import Model


load_dotenv()
PATH = str(os.getenv("MODEL"))
print(PATH)
def new_text_callback(text: str):
    print(text, end="", flush=True)


LLAMA_CONTEXT_PARAMS_SCHEMA = {"use_mlock": {
        "type": bool,
        "description": "force system to keep model in RAM",
        "options": None,
        "default": 0,
    }}
model = Model(ggml_model=PATH, n_ctx=512)

# all cogs inherit from this base class
class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot # adding a bot attribute for easier access

    # adding a command to the cog
    @commands.command(name="ping")
    async def pingcmd(self, ctx):
        """the best command in existence"""
        await ctx.send(ctx.author.mention)
    
    # adding a slash command to the cog (make sure to sync this!)
    @app_commands.command(name="ping")
    async def slash_pingcmd(self, interaction):
        """the second best command in existence"""
        await interaction.response.send_message(interaction.user.mention)

    @app_commands.command(name="chat")
    async def chat(self,interaction: discord.Interaction,msg:str):
        """the 0th best command in existence"""
        await interaction.response.send_message("typing..")
        channel = interaction.channel
        async with channel.typing():
            text = model.generate(str(msg), n_predict=128, new_text_callback=new_text_callback, n_threads=8, interactive=True)
            await interaction.channel.send(text)
        

# usually you’d use cogs in extensions
# you would then define a global async function named 'setup', and it would take 'bot' as its only parameter


async def setup(bot):
    # finally, adding the cog to the bot
    await bot.add_cog(General(bot=bot))
