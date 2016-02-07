# -*- coding: utf-8 -*-
import telebot
import random
from SQLighter import SQLighter
import config
import utils

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["test"])
def find_file_ids(message):
    for file in os.listdir("music/"):
        if file.split(".")[-1] == "ogg":
            f = open(file, 'rb')
            bot.send_voice(message.chat.id, f, None)
        time.sleep(3)


@bot.message_handler(commands=["game"])
def game(message):
    # Подключаемся к БД
    db_worker = SQLighter(config.database_name)
    # Получаем случайную строку из БД
    row = db_worker.select_single(random.randint(1, utils.get_rows_count()))
    # Формируем разметку
    markup = utils.generate_markup(row[2], row[3])
    # Отправляем аудиофайл с вариантами ответа
    bot.send_voice(message.chat.id, row[1], reply_markup=markup)
    # Включаем игровой режим
    utils.set_user_game(message.chat.id, row[2])
    # Отсоединяемся от БД
    db_worker.close()


@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
    # Если функция возвращает None -> Человек не в игре
    answer = utils.get_answer_for_user(message.chat.id)
    # Как вы помните, answer может быть либо текст, либо None
    # Если None:
    if not answer:
        bot.send_message(message.chat.id, 'Чтобы начать игру, выберите команду /game')
    else:
        # Уберем клавиатуру с вариантами ответа.
        keyboard_hider = types.ReplyKeyboardHide()
        # Если ответ правильный/неправильный
        if message.text == answer:
            bot.send_message(message.chat.id, 'Верно!', reply_markup=keyboard_hider)
        else:
            bot.send_message(message.chat.id, 'Увы, вы не угадали. Попробуйте ещё раз!', reply_markup=keyboard_hider)
        # Удаляем юзера из хранилища (игра закончена)
        utils.finish_user_game(message.chat.id)


if __name__ == '__main__':
    utils.count_rows()
    random.seed()
    bot.polling(none_stop = True)
