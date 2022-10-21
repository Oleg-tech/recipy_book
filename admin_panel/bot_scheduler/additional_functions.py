import requests

from admin_panel.models import Users, Recipes


def create_new_user(user_id, first_name, last_name, username):
    user = Users.objects.create(id=user_id, first_name=first_name, last_name=last_name, username=username)
    user.save()


def check_creation(user_id):
    return Users.objects.get(pk=user_id)


def check_exsistance(user_id):
    user = Users.objects.all().filter(id=user_id).exists()
    return user


def create_recipe(user_id, text):
    recipe = Recipes.objects.create(name=text, discription="", user_id=user_id)
    recipe.save()


def get_information_about_user(user_id):
    user = Users.objects.get(id=user_id)
    info = f"Ім'я:  {user.register_name}\n"
    info += f"Стать: {user.sex}\n"
    return info


def download_image(url, id):
    recipe = list(Recipes.objects.values_list('name', flat=True).filter(id=id))[0]

    try:
        response = requests.get(url, stream=True)

        if response.status_code == 200:
            with open(f'admin_panel/static/images/{recipe}.jpg', 'wb') as f:
                f.write(response.content)
        else:
            print(response.status_code)
    except:
        Recipes.objects.filter(id=id).update(image=None)
        print('Failed')
