from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .bot_scheduler.additional_functions import download_image
from .forms import *
from .models import Users, Recipes


class AdminLoginView(LoginView):
    form_class = LoginForm
    template_name = 'admin_panel/login.html'


class UsersTableView(ListView):
    model = Users
    template_name = 'admin_panel/users.html'
    context_object_name = 'users'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'full_path': 'users/',
        })

        return context


class RecipesTableView(ListView):
    model = Recipes
    template_name = 'admin_panel/recipes.html'
    context_object_name = 'recipes'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'full_path': 'recipes/',
        })

        return context


class CreateRecipe(CreateView):
    template_name = 'admin_panel/add_recipe.html'
    model = Recipes
    success_url = "/recipes/"
    form_class = AddRecipeForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

            new_id = Recipes.objects.values_list('id', flat=True).filter(name=form['name'].value())[0]
            download_image(form['image'].value(), new_id)

            return redirect(self.success_url)

        return render(request, self.template_name, {'form': form})


def edit_recipe(request, id_of_recipe):
    initial = Recipes.objects.get(id=id_of_recipe)
    form = AddRecipeForm()

    context = {
        'form': form,
        'csrf_token': (request.POST.get('csrfmiddlewaretoken')),
    }

    if request.POST:
        form = AddRecipeForm(request.POST, instance=initial)
        if form.is_valid():
            form.save()
            return redirect('recipes')

    return render(request, 'admin_panel/edit_recipe.html', context)


def delete_recipe(request):
    recipe_id = request.POST.get('post_id')
    Recipes.objects.filter(id=recipe_id).delete()

    return JsonResponse({'data': '', 'csrfmiddlewaretoken': request.POST.get('csrfmiddlewaretoken')})


# class CreateRecipeView(CreateView):
#     template_name = 'admin_panel/add_recipe.html'
#     model = Recipes
#     fields = ['name', 'discription', 'image']
#     success_url = "/recipes/"
