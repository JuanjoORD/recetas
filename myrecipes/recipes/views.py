from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Recipe, Ingredient, Process
from .serializers import UserSerializer, RecipeSerializer, IngredientSerializer, ProcessSerializer

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ReportTime(request, *args, **kwargs):


    return Response(data="Only authenticated users", status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ReportQuantity(request, *args, **kwargs):
    return Response(data="Only authenticated users", status=status.HTTP_200_OK)


#CRUD Recipe
class RecipeListView(ListAPIView):
    serializer_class = RecipeSerializer
    permission_classes = ()
    queryset = Recipe.objects.all()


@permission_classes([IsAuthenticated])
class RecipeCreateView(CreateAPIView):
    serializer_class = RecipeSerializer
    permission_classes = ()


class RecipeRetrieveView(RetrieveAPIView):
    serializer_class = RecipeSerializer
    permission_classes = ()
    queryset = Recipe.objects.all()
    lookup_field = 'id'

@permission_classes([IsAuthenticated])
class RecipeUpdateView(UpdateAPIView):
    serializer_class = RecipeSerializer
    permission_classes = ()
    queryset = Recipe.objects.all()
    lookup_field = 'id'


#CRUD Ingredient
class IngredientListView(ListAPIView):
    serializer_class = IngredientSerializer
    permission_classes = ()
    queryset = Ingredient.objects.all()

@permission_classes([IsAuthenticated])
class IngredientCreateView(CreateAPIView):
    serializer_class = IngredientSerializer
    permission_classes = ()


class IngredientRetrieveView(RetrieveAPIView):
    serializer_class = IngredientSerializer
    permission_classes = ()
    queryset = Ingredient.objects.all()
    lookup_field = 'id'

@permission_classes([IsAuthenticated])
class IngredientUpdateView(UpdateAPIView):
    serializer_class = IngredientSerializer
    permission_classes = ()
    queryset = Ingredient.objects.all()
    lookup_field = 'id'


#CRUD Process
class ProcessListView(ListAPIView):
    serializer_class = ProcessSerializer
    permission_classes = ()
    queryset = Process.objects.all()

@permission_classes([IsAuthenticated])
class ProcessCreateView(CreateAPIView):
    serializer_class = ProcessSerializer
    permission_classes = ()


class ProcessRetrieveView(RetrieveAPIView):
    serializer_class = ProcessSerializer
    permission_classes = ()
    queryset = Process.objects.all()
    lookup_field = 'id'

@permission_classes([IsAuthenticated])
class ProcessUpdateView(UpdateAPIView):
    serializer_class = ProcessSerializer
    permission_classes = ()
    queryset = Process.objects.all()
    lookup_field = 'id'