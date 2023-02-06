import os

import discord
import asyncio
from discord import app_commands
from discord.ext import commands
from chatgpt import get_response
from loguru import logger


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        try:
            synced = await bot.tree.sync()
            logger.success(f"Synced {len(synced)} commands!")
        except Exception as e:
            logger.error(f"errors: {e}")

    @bot.tree.command(name="ask")
    @app_commands.describe(message="Ask me anything Dota related!")
    async def ask(interaction: discord.Interaction, message: str):
        await interaction.response.defer()
        await asyncio.sleep(5)
        response = get_response(message)
        await interaction.followup.send(response)
        logger.success(f"Successfully sent message: {response}")

    bot.run(os.getenv("DISCORD_TOKEN"))
