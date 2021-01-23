from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password', 'first_name','last_name','phone')

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ('id', 'email', 'username')

class MyProcessSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Process
        fields = ('id', 'quantity', 'time_min')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'ingredient_name')


class RecipeSerializer(serializers.ModelSerializer):
    #user = UserSerializer(read_only=True)
    ingredients = IngredientSerializer(many=True, read_only=True) 
    class Meta:
        model = Recipe
        fields = ('id', 'recipe_name', 'ingredients')


class ProcessSerializer(serializers.ModelSerializer):
    #ingredient = IngredientSerializer(read_only=True)
    #recipe = RecipeSerializer(read_only=True)

    class Meta:
        model = Process
        fields = ('id', 'quantity', 'time_min', 'steps')