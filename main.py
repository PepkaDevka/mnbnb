import telebot
import pyowm
from telebot import types
#Tokens for bot#
owm = pyowm.OWM('bda173983047355bed9c98ea77f95b01')
bot = telebot.TeleBot('860947749:AAGrxOdqAiTVIG2xftl5WiX32BTu-UnFOYA')
#---------------------------------------------------------------------#

#keyboards variable
general_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard =True, one_time_keyboard =False)


#Place find
observation = owm.weather_at_place('Poltava,UA')
w = observation.get_weather()
t = w.get_temperature('celsius')['temp']
a = int(t)
b = str(a)
print(t)



#start bot function

@bot.message_handler(content_types = ['text'])
def starting(message):
	if message.text == '/start':
		general_keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
		general_keyboard.row('Погода🌦')
		bot.send_message(message.chat.id, 'Привіт, ' + str(message.from_user.first_name)+ '!', reply_markup = general_keyboard)
		bot.register_next_step_handler(message, general_func)


@bot.message_handler(content_types = ['text'])
def general_func(message):
	if message.text == 'Погода🌦':
		weather_find(message)


def weather_find(message):
	global b
	if int(b) < 15:
		bot.send_message(message.chat.id, 'Погода зараз: '+str(b)+'°C'+'\n'+'Вдягайся тепліше, друже🥶')
		bot.register_next_step_handler(message, general_func)
	if int(b) <= 0:
		bot.send_message(message.chat.id, 'Погода зараз: '+str(b)+'°C'+'\n'+'Морозець🥶! Куртка з ботинками твої кращі друзі на сьогодні💪')
	if int(b) >= 15 and int(b) <= 25:
		bot.send_message(message.chat.id, 'Погода зараз: '+str(b)+'°C'+'\n'+'Зараз не холодно, вдягайся як заманеться!')



bot.infinity_polling(none_stop = True)
