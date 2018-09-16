from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import calculator

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    mybot = Updater(open("key", "r").read(), request_kwargs=PROXY)

    # calculator
    mybot.dispatcher.add_handler(CommandHandler("calc", calc))
    # word counter
    mybot.dispatcher.add_handler(CommandHandler("wordcount", word_count))

    mybot.start_polling()
    mybot.idle()


def word_count(bot, update):
    user_text = update.message.text
    print(user_text)
    if user_text.strip() == '/wordcount':
        result = 0
    else:
        output = update.message.text

        # find left bracket, delete everything before.
        output = output[output.index('"') + 1:]

        # find next bracket, delete everything after.
        output = output[:output.index('"')]

        result = len(output.split())

    update.message.reply_text(result)


def calc(bot, update):
    user_text = update.message.text.replace("/calc", "")

    result = calculator.calculator(user_text)

    update.message.reply_text(result)

# Вызываем функцию - эта строчка собственно запускает бота
main()
