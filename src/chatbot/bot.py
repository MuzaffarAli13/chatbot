import chainlit as cl
from chatbot.main import myAgent
import asyncio

@cl.on_chat_start
async def chat_start():
    await cl.Message("Hello How I can Help you?").send()

@cl.on_message
async def main(message: cl.Message):
    user_input = message.content
    response = asyncio.run(myAgent(user_input))
    await cl.Message(
        content=f"{response}",
    ).send()
