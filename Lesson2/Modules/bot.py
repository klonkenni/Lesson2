from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import datetime
import logging
import json

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    mybot = Updater(open("key", "r").read(), request_kwargs=PROXY)

    mybot.dispatcher.add_handler(CommandHandler("ephem", greet_user))
    mybot.dispatcher.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


def greet_user(bot, update):
    user_text = update.message.text
    splited_user_text = user_text.split(" ")
    print(splited_user_text)
    try:
        planet_object = getattr(ephem, splited_user_text[1])
    except AttributeError:
        planet_object = getattr(ephem, "Mars")
        update.message.reply_text("There is no such planet. So let it be Mars:")

    now = datetime.datetime.now().date()
    pl = planet_object(now)
    constellation = ephem.constellation(pl)
    update.message.reply_text(constellation)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)



# Вызываем функцию - эта строчка собственно запускает бота
main()