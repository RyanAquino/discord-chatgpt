import os

import discord
import asyncio
from discord import app_commands
from discord.ext import commands
from chatgpt import get_response
from loguru import logger


def run_discord_bot():
    bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

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
        response = get_response(message)
        await interaction.response.defer(thinking=True)
        await asyncio.sleep(30)
        await interaction.followup.send(response)
        logger.success(f"Successfully sent message: {response}")

    bot.run(os.getenv("DISCORD_TOKEN"))
