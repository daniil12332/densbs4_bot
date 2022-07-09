import requests
from bs4 import BeautifulSoup
import telebot

bot = telebot.TeleBot("5467348981:AAGzIrGEbuQuIMeAcY85fp7C3IUClbdR9uw")
url = "https://pogoda.mail.ru/prognoz/moskva/"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")
tag = soup.find("div", class_="information__content__temperature").text

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, "Weather bot is started.")

@bot.message_handler(commands=["weather"])
def handle_text(message):
    bot.send_message(message.chat.id, tag + " in Moscow.")

bot.polling(none_stop=True, interval=0)