from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(null=True, max_length=255)
    REQUIRED_FIELDS = [
        'username',
        'phone',
        'first_name',
        'last_name',
    ]

    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email


class Ingredient(models.Model):
    ingredient_name    = models.CharField(max_length=60)    

    def __str__(self):
        return self.ingredient_name


class Recipe(models.Model):
    recipe_name  =   models.CharField(max_length=40)
    ingredients   = models.ManyToManyField(Ingredient, through='Process')
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

    def __str__(self):
        return self.recipe_name


class Process (models.Model):    
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=True, null=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField()
    time_min = models.PositiveIntegerField()
    steps = models.TextField(blank=True)

    def __str__(self):
        return self.steps

class ProcessInLine(admin.TabularInline):
    model = Process
    extra = 1


class IngredientAdmin(admin.ModelAdmin):
    inlines = (ProcessInLine,)


class RecipeAdmin (admin.ModelAdmin):
    inlines = (ProcessInLine,)