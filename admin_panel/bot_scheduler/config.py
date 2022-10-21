from admin_panel.models import Recipes
import telebot

dish_names = [i for i in Recipes.objects.values_list('name', flat=True)]

bot = telebot.TeleBot('1842681158:AAHQSl6sn47NdaNk3Gf29nHIf8nL3X9DDeA')


keyboard_user_sex = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard_user_sex.row('Чоловік').row('Жінка')

keyboard_menu = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard_menu.row('Про мене').row('Рецепти')

keyboard_recepies = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
keyboard_recepies.row("На головну")

keyboard_personal = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
