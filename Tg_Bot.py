import telebot
from telebot import types
import get_lessons
import config

bot = telebot.TeleBot(config.Token)

#Стартовое сообщение
@bot.message_handler(commands=['start'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)

	item1 = types.KeyboardButton("/пара")
	item2 = types.KeyboardButton("/расписание")
	item3 = types.KeyboardButton("/неделя")
	item4 = types.KeyboardButton("!1 неделя")
	item5 = types.KeyboardButton("!2 неделя")
	item6 = types.KeyboardButton("/help")
	item7 = types.KeyboardButton("/завтра")
	markup.add(item1,item2, item3, item6, item7)

	bot.send_message(message.chat.id, "Привет, {0.first_name}, я бот-помощник с расписанием.\n Вот список моих команд:\n /help - узнать список команд\n /пара - узнать, какая сейчас пара.\n /расписание - узнать какое сегодня расписание\n <b>/завтра</b> - узнать расписание на завтра\n /неделя - узнать все расписание на неделю\n".format(message.from_user), parse_mode = 'html', reply_markup=markup)

#Сообщение со всеми командами
@bot.message_handler(commands=['help'])
def send_help(message):

	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)

	item1 = types.KeyboardButton("/пара")
	item2 = types.KeyboardButton("/расписание")
	item3 = types.KeyboardButton("/неделя")
	item4 = types.KeyboardButton("!1 неделя")
	item5 = types.KeyboardButton("!2 неделя")
	item6 = types.KeyboardButton("/help")
	item7 = types.KeyboardButton("/завтра")
	markup.add(item1,item2, item3, item6, item7)

	bot.send_message(message.chat.id, "<b>Вот список моих команд:\n   /пара</b> - узнать, какая сейчас пара.\n   <b>/расписание</b> - узнать какое сегодня расписание\n   <b>/завтра</b> - узнать расписание на завтра\n   <b>/неделя</b> - узнать все расписание на текущую неделю\n<b>     [ !1 неделя</b> - узнать расписание на первую неделю<b> ]\n     [ !2 неделя</b> - узнать расписание на первую неделю ]", parse_mode = "html", reply_markup=markup)

#Сообщение с расписанием текущей пары
@bot.message_handler(commands=['пара'])
def send_lessons(message):
	lesson = get_lessons.get_lessons()
	if lesson == "lessons will start":
		first_lesson = get_lessons.get_first_lessons()
		bot.send_message(message.chat.id, "<b>Пары еще не начались!\nПервая пара:</b> {0}\n<b>Начало в:</b> {1}".format(first_lesson.name,first_lesson.time_start), parse_mode = 'html')
	elif lesson == "lessons are over":
		bot.send_message(message.chat.id, "<b>Пары кончились!</b>", parse_mode = 'html')
	elif lesson == "pause":
		next_lesson = get_lessons.get_next_lessons()
		bot.send_message(message.chat.id, "<b>Сейчас перемена\nСледующая пара:</b> {0}\n<b>Начало в:</b> {1}".format(next_lesson.name,next_lesson.time_start), parse_mode = 'html')
	elif lesson == "no lesson":
		bot.send_message(message.chat.id, "<b>На сегодня пар нет, отдыхай!</b>", parse_mode = 'html')
	else:
		bot.send_message(message.chat.id, "Сейчас идет пара {0}\nНачало пары: {1}\nКонец пары: {2}\nАудитория: {3}".format(lesson.name, lesson.time_start, lesson.time_end,lesson.auditorium))

#Сообщение с расписанием на сегодняшний день
@bot.message_handler(commands=['расписание'])
def send_schedule(message):
	text = get_lessons.get_all_lessons_today()
	bot.send_message(message.chat.id, "<b>Все пары на сегодня:</b>\n{0}".format(text), parse_mode = 'html')

#Сообщение с расписанием на текущую неделю
@bot.message_handler(commands=['неделя'])
def send_week(message):
	text = get_lessons.get_all_lessons_weeks("")
	bot.send_message(message.chat.id, "<b>Все расписание на неделю:</b>\n{0}".format(text), parse_mode = 'html')

#Сообщение с расписанием на первую неделю
@bot.message_handler(commands=['1неделя'])
def send_first_week(message):
	text = get_lessons.get_all_lessons_weeks("Первая")
	bot.send_message(message.chat.id, "<b>Все расписание на неделю:</b>\n{0}".format(text), parse_mode = 'html')

#Сообщение с расписанием на вторую неделю
@bot.message_handler(commands=['2неделя'])
def send_second_week(message):
	text = get_lessons.get_all_lessons_weeks("Вторая")
	bot.send_message(message.chat.id, "<b>Все расписание на неделю:</b>\n{0}".format(text), parse_mode = 'html')

#Сообщение с расписанием на завтра
@bot.message_handler(commands=['завтра'])
def send_lessons_tomorrow(message):
	text = get_lessons.get_all_lessons_tomorrow()
	bot.send_message(message.chat.id, "<b>Все пары на завтра:</b>\n{0}".format(text), parse_mode = 'html')

#Обработка сообщений с командами в другом виде
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	if message.text == "!1 неделя" or message.text == "!1 Неделя" or message.text == "!1Неделя" or message.text == "!1неделя":
		send_first_week(message)
	elif message.text == "!2 неделя" or message.text == "!2 Неделя" or message.text == "!2Неделя" or message.text == "!2неделя":
		send_second_week(message)
	elif message.text == "!расписание" or message.text == "!Расписание":
		send_schedule(message)
	elif message.text == "!пара" or message.text == "!Пара":
		send_lessons(message)

bot.infinity_polling()