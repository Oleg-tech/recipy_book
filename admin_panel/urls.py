from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import *


urlpatterns = [
    path('login/', AdminLoginView.as_view(), name='login'),
    path('users/', login_required(UsersTableView.as_view()), name="users"),
    path('recipes/', login_required(RecipesTableView.as_view()), name="recipes"),
    path('add-recipe/', login_required(CreateRecipe.as_view()), name='add_recipe'),
    path('edit-recipe/<int:id_of_recipe>', login_required(edit_recipe), name='edit_recipe'),
    path('delete-recipe', login_required(delete_recipe), name='delete_recipe'),
]
