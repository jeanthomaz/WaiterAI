import os
import openai

from dotenv import load_dotenv
from random import choice
from flask import Flask, request

load_dotenv()
open.api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\\nWaiter:"
restart_sequence = "\\n\\nCliente:"
session_prompt = "Você está conversando com o Waiter, um bot especializado em atender clietes do bar Rei dos Salgadinhos.\n\nCliente: Quem é você?\nWaiter: Sou Waiter, seu atendente do Rei dos Salgadinhos,. Como posso ajudá-lo?\n\nCliente: Qual é o cardápio?\nWaiter: Temos uma grande variedade de salgadinhos, como bolinha de queijo, coxinha de frango, coxinha de frango com catupiry, enroladinho de queijo e presunto frito, enroladinho de queijo e presunto assado, enroladinho de salsicha, croquete de carne, kibe, risoli de camarão, risoli de carne, empada de frango, empada de palmito, empada de camarão, pastel assado de frango, esfiha de carne, espeto de frango"

def ask(question, chat_log=None):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= prompt_text,
    temperature=0.3,
    max_tokens=256,
    top_p=0.5,
    frequency_penalty=0,
    presence_penalty=0
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interraction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'