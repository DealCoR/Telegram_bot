import random
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
from telebot import types
import Alex_Ovechkin8

token = '2008007638:AAFa-UKK9o84URQd4hdlPycAgJHPs3OLOUQ'
bot = telebot.TeleBot(token)


# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Привет":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе статистику Александра Овечкина.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_game = types.InlineKeyboardButton(text='Games', callback_data='Games')
        # И добавляем кнопку на экран
        keyboard.add(key_game)
        key_goals = types.InlineKeyboardButton(text='Goals', callback_data='Goals')
        keyboard.add(key_goals)
        key_asists = types.InlineKeyboardButton(text='Asists', callback_data='Asists')
        keyboard.add(key_asists)
        key_points = types.InlineKeyboardButton(text='Points', callback_data='Points')
        keyboard.add(key_points)
        key_poleznost = types.InlineKeyboardButton(text='+/-', callback_data='+/-')
        keyboard.add(key_poleznost)
        key_gretzky = types.InlineKeyboardButton(text='Goals to Gretzky', callback_data='goal_1')
        keyboard.add(key_gretzky)
        key_howe = types.InlineKeyboardButton(text='Goals to Howe', callback_data='goal_2')
        keyboard.add(key_howe)
        key_jagr = types.InlineKeyboardButton(text='Goals to Jagr', callback_data='goal_3')
        keyboard.add(key_jagr)
        key_old = types.InlineKeyboardButton(text='Age', callback_data='Age')
        keyboard.add(key_old)
        key_power = types.InlineKeyboardButton(text='Powerplay goals', callback_data='power')
        keyboard.add(key_power)

        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери интересующую статистику', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == "Games":

        msg = Alex_Ovechkin8.stata[0] + ' games played'      # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)

    if call.data == "Goals":

        msg = Alex_Ovechkin8.stata[1] + ' goals scored'  # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)

    if call.data == "Asists":

        msg = Alex_Ovechkin8.stata[2] + ' asists'  # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)

    if call.data == "Points":
        msg = Alex_Ovechkin8.stata[3] + ' points'  # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)

    if call.data == "+/-":
        msg = Alex_Ovechkin8.stata[4] + ' +/-'  # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)

    if call.data == "goal_1":
        msg = Alex_Ovechkin8.stata[5] + ' goals to Wayne Gretzky'  # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)

    if call.data == "goal_2":
        msg = Alex_Ovechkin8.stata[6] + ' goals to Gordy Howe'  # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)

    if call.data == "goal_3":
        msg = Alex_Ovechkin8.stata[7] + ' goals to Jaromir Jagr'  # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)

    if call.data == "Age":
        msg = Alex_Ovechkin8.stata[8] + ' years old'  # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)

    if call.data == "power":
        msg = Alex_Ovechkin8.stata[9] + ' power play goals'  # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)


# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)


