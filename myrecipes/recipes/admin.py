from django.contrib import admin
from .models import Recipe, Ingredient, Process, User, IngredientAdmin, RecipeAdmin

admin.site.register(User)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
# Register your models here.