from django.shortcuts import render
from django.views.generic import TemplateView


class IngredientsCreateFormView(TemplateView):
    template_name = 'ingredients_create_form.html'

    
class IngredientsDetailView(TemplateView):
    template_name = 'ingredients_detail.html'

    
class IngredientsListView(TemplateView):
    template_name = 'ingredients_list.html'

    
class IngredientsUpdateFormView(TemplateView):
    template_name = 'ingredients_update_form.html'

    
class OrdersCreateFormView(TemplateView):
    template_name = 'orders_create_form.html'

    
class OrdersDetailView(TemplateView):
    template_name = 'orders_detail.html'

    
class OrdersListView(TemplateView):
    template_name = 'orders_list.html'

    
class OrdersUpdateFormView(TemplateView):
    template_name = 'orders_update_form.html'

    
class RecipesCreateFormView(TemplateView):
    template_name = 'recipes_create_form.html'

    
class RecipesDetailView(TemplateView):
    template_name = 'recipes_detail.html'

    
class RecipesListView(TemplateView):
    template_name = 'recipes_list.html'

    
class RecipesUpdateFormView(TemplateView):
    template_name = 'recipes_update_form.html'
