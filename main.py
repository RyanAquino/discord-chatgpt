import os
import openai
from dotenv import load_dotenv
from bot import run_discord_bot
from loguru import logger


def main():
    load_dotenv()
    openai.api_key = os.getenv("OPENAPI_API_KEY")
    logger.success("App initialized!")
    run_discord_bot()


if __name__ == '__main__':
    main()
