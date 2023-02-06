from loguru import logger
import openai


def get_response(message: str) -> str:
    model_engine = "text-davinci-003"
    logger.debug(f"Prompt: {message}")
    response = openai.Completion.create(
        model=model_engine,
        prompt=message,
        temperature=0.6,
        max_tokens=512
    )
    logger.debug(f"ChatGPT Response: {response}")

    return response.choices[0].text.strip()
