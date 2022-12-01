'''
# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


import asyncio
asyncio.run(bot.polling())
'''

import os
from telebot.async_telebot import AsyncTeleBotimport telebot
from dotenv import load_dotenv

load_dotenv()

chave = os.getenv('TOKEN')

bot = AsyncTeleBot(chave, parse_mode="HTML")

textol1 = """</b><code>, como eu posso te ajudar?

Você gostaria de ver o nosso</code>
📒  /portfolio <code>de soluções ou entrar em </code>
📞  /contato<code>?

Clique em alguma opção acima ou no menu aqui embaixo.</code>
👇"""

textol2 = """</b><code>, segue nosso portfólio:</code>

🤖  /chatbot <code>=> Tenha um chat bot parecido com este;</code>

🌎  /site <code>=> Criamos o seu site;</code>

💻  /appweb <code>=> Projetamos a sua aplicação WEB</code>

📱  /appmobile <code>=> Desenvolvemos o seu aplicativo mobile</code>



🔙  /start <code>=> Voltar</code>
"""

textol3 = """</b><code>, segue nossos contatos:

🌎  Site => </code>www.gtk.dev.br<code>

📧  E-mail => </code>contato@gtk.dev.br<code>

📞  Telefone => 11998265860</code>



🔙  /start <code>=> Voltar</code>
"""

textol4 = """</b><code>, tenha um chat bot para te auxiliar no relacionamento com seu cliente.
 
Automatize as respostas para as perguntas mais frequentes.
 
Tenha um atendimento 24 horas. 

Entre em </code>/contato <code> para criarmos um orçamento personalizado.</code>



🔙  /start <code>=> Voltar</code>
"""

textol5 = """</b><code>, tenha o seu próprio site, com e-mail </code>@nomedoseusite.com.br<code>, para passar mais credibilidade do seu negócio.

Utilizamos linguagens de programação modernas, que se adaptam as diversas telas (PC, Tablet ou Smartphone).

Veja um exemplo de site em: </code>www.gtk.dev.br/exemplo<code> 

Entre em </code>/contato <code> para criarmos um orçamento personalizado.</code>



🔙  /start <code>=> Voltar</code>
"""

textol6 = """</b><code>, tenha a sua própria aplicação WEB, com acesso a banco de dados.

As aplicações que rodam nos navegadores geralmente são mais leves, não precisando de computadores ("hardware") muito avançados.

Pode ser acessado de qualquer lugar com internet.

Entre em </code>/contato <code> para criarmos um orçamento personalizado.</code>



🔙  /start <code>=> Voltar</code>
"""

textol7 = """</b><code>, tenha o seu próprio APP (no momento apenas para o sistema Android).

Criamos o seu APP com acesso a banco de dados; utilizamos os recursos do smartphone como GPS, camera, microfone, etc.  

Entre em </code>/contato <code> para criarmos um orçamento personalizado.</code>



🔙  /start <code>=> Voltar</code>
"""

@bot.message_handler(commands=["start"])
async def start(mensagem):
  await bot.send_message(mensagem.chat.id, "<code>Olá </code><b>" + mensagem.from_user.first_name + textol1)

@bot.message_handler(commands=["portfolio"])
async def portfolio(mensagem):
  await bot.send_message(mensagem.chat.id, "<b>" + mensagem.from_user.first_name + textol2)

@bot.message_handler(commands=["contato"])
async def contato(mensagem):
  await bot.send_message(mensagem.chat.id, "<b>" + mensagem.from_user.first_name + textol3)

@bot.message_handler(commands=["chatbot"])
async def chatbot(mensagem):
  await bot.send_message(mensagem.chat.id, "<b>" + mensagem.from_user.first_name + textol4)

@bot.message_handler(commands=["site"])
async def site(mensagem):
  await bot.send_message(mensagem.chat.id, "<b>" + mensagem.from_user.first_name + textol5)

@bot.message_handler(commands=["appweb"])
async def appweb(mensagem):
  await bot.send_message(mensagem.chat.id, "<b>" + mensagem.from_user.first_name + textol6)

@bot.message_handler(commands=["appmobile"])
async def appmobile(mensagem):
  await bot.send_message(mensagem.chat.id, "<b>" + mensagem.from_user.first_name + textol7)

async def verificar(mensagem):
  return True

@bot.message_handler(func=verificar)
async def responder(mensagem):
  await bot.reply_to(
    mensagem, mensagem.from_user.first_name +
    ", não utilize o teclado, clique apenas nas opções que aparecem nas mensagens, precedidas por uma barra."
  )

import asyncio
asyncio.run(bot.polling())
