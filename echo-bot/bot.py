import config
import telebot

def listener(messages):
    '''
    receives incoming messages
    '''
    for m in messages:
        if m.content_type == 'text':
            bot.send_message(m.chat.id, m.text)

if __name__ == '__main__':
    bot = telebot.TeleBot(config.token)
    bot.set_update_listener(listener)
    bot.polling(none_stop = True)
