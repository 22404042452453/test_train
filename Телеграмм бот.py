import telebot
from new_token import token
import os
from craft_image import new_pictures

bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=['start', 'info'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, я бот который создан для прохождения тестового задания\n"
                                      "Загрузите свое изображение!!!")


@bot.message_handler(content_types='text')
def message_reply(message):
    bot.send_message(message.chat.id, 'Я не люблю разговаривать с людьми')


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        if not os.path.isdir("pictures"):
            os.mkdir("pictures")

        os.chdir("pictures")

        with open('photo.jpeg', 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, "Фото получил, обрабатываю...")
        os.chdir("../")

        new_pictures()

        for i in os.listdir('.'):

            bot.send_photo(message.chat.id, photo=open(i, 'rb'), caption="Ваша фотография без фона")
            os.remove(i)
            os.chdir("../")

    except Exception as ex:

        bot.reply_to(message, "Что-то пошло не так, пожалуйста повторите отправку!!!")


bot.polling(non_stop=True)
