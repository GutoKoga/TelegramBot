import os
import telebot
from dotenv import load_dotenv

load_dotenv()

chave = os.getenv('TOKEN')

bot = telebot.TeleBot(chave, parse_mode="HTML")

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
def start(mensagem):
  bot.send_message(mensagem.chat.id, "<code>Olá </code><b>" + mensagem.from_user.first_name + textol1)

@bot.message_handler(commands=["portfolio"])
def portfolio(mensagem):
  bot.send_message(mensagem.chat.id, "<b>" + mensagem.from_user.first_name + textol2)

@bot.message_handler(commands=["contato"])
def contato(mensagem):
  bot.send_message(mensagem.chat.id, "<b>" + mensagem.from_user.first_name + textol3)

@bot.message_handler(commands=["chatbot"])
def chatbot(mensagem):
  bot.send_message(mensagem.chat.id, "<b>" + mensagem.from_user.first_name + textol4)

@bot.message_handler(commands=["site"])
def site(mensagem):
  bot.send_message(mensagem.chat.id, "<b>" + mensagem.from_user.first_name + textol5)

@bot.message_handler(commands=["appweb"])
def appweb(mensagem):
  bot.send_message(mensagem.chat.id, "<b>" + mensagem.from_user.first_name + textol6)

@bot.message_handler(commands=["appmobile"])
def appmobile(mensagem):
  bot.send_message(mensagem.chat.id, "<b>" + mensagem.from_user.first_name + textol7)

def verificar(mensagem):
  return True

@bot.message_handler(func=verificar)
def responder(mensagem):
  bot.reply_to(
    mensagem, mensagem.from_user.first_name +
    ", não utilize o teclado, clique apenas nas opções que aparecem nas mensagens, precedidas por uma barra."
  )

bot.infinity_polling()
