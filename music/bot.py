# -*- coding: utf-8 -*-
import telebot

bot = telebot.Telebot(config.token)

@bot.message_handler(commands=["test"])
def find_file_ids(message):
    for file in os.listdir("music/"):
        if file.split(".")[-1] == "ogg":
            f = open(file, 'rb')
            bot.send_voice(message.chat.id, f, None)
        time.sleep(3)


if __name__ == '__main__':
    bot.polling(none_stop = True)