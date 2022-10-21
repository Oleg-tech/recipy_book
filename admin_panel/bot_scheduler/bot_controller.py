import os

from admin_panel.models import Users
from .additional_functions import check_exsistance, create_new_user, get_information_about_user
from .config import *


@bot.message_handler(commands=['help'])
def send_welcome(msg):
    info_for_user = "Привіт, це бот \"Книга рецептів\".\nЩоб розпочати введіть команду /start та пройдіть реєстрацію."
    bot.send_message(msg.chat.id, info_for_user, reply_markup=keyboard_menu)


@bot.message_handler(commands=['start'])
def send_welcome(msg):
    if not check_exsistance(msg.from_user.id):
        create_new_user(msg.from_user.id, msg.from_user.first_name, msg.from_user.last_name, msg.from_user.username)
        bot.reply_to(msg, "Привіт, це бот \"Книга рецептів\"\nВведіть своє ім'я:")
    if not list(Users.objects.values_list('register_name', flat=True).filter(id=msg.from_user.id))[0]:
        bot.reply_to(msg, "Завершіть реєстрацію.\nВведіть своє ім'я:")
    else:
        bot.reply_to(msg, "Ви вже зареєстровані", reply_markup=keyboard_menu)


@bot.message_handler(content_types=["text"])
def message(msg):
    if not list(Users.objects.values_list('register_name', flat=True).filter(id=msg.from_user.id))[0]:
        Users.objects.filter(pk=msg.from_user.id).update(register_name=msg.text)
        bot.reply_to(msg, "Вкажіть свою стать", reply_markup=keyboard_user_sex)

    elif not list(Users.objects.values_list('sex', flat=True).filter(id=msg.from_user.id))[0]:
        if msg.text.lower() == "чоловік" or msg.text.lower() == "жінка":
            Users.objects.filter(pk=msg.from_user.id).update(sex=msg.text)
            bot.send_message(msg.chat.id, "Вітаємо з успішною реєстрацією", reply_markup=keyboard_menu)
        else:
            bot.reply_to(msg, "Неправильно введена стать\nСпробуйте ще раз", reply_markup=keyboard_user_sex)

    else:
        if msg.text == "Про мене":
            info = get_information_about_user(msg.from_user.id)
            bot.send_message(msg.chat.id, info, reply_markup=keyboard_menu)

        if msg.text == "Рецепти":
            for recipe in Recipes.objects.values_list('name', flat=True):
                keyboard_recepies.row(recipe)

            available_recipes = "Доступні рецепти:"
            count = 1
            for i in dish_names:
                available_recipes += f"\n{count}. {i}"
                count += 1

            bot.send_message(msg.chat.id, available_recipes, reply_markup=keyboard_recepies)

        if msg.text == 'На головну':
            bot.send_message(msg.chat.id, "Головне меню", reply_markup=keyboard_menu)

        if msg.text in dish_names:
            dish = Recipes.objects.filter(name=msg.text).first()
            if os.path.exists(f'admin_panel/static/images/{msg.text}.jpg'):
                with open(f'admin_panel/static/images/{msg.text}.jpg', 'rb') as img:
                    bot.send_photo(msg.chat.id, img)
            bot.send_message(msg.chat.id, dish.name+'\n'+dish.discription, reply_markup=keyboard_recepies)


def main_polling():
    print("The bot is running")
    bot.infinity_polling()
