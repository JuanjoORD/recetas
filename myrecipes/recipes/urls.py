from django.contrib import admin
from django.urls import path, include
from recipes import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    #path('report/', views.restricted),    
    
    path('recipe/', views.RecipeListView.as_view(), name='recipe'),
    path('recipe/create/', views.RecipeCreateView.as_view(), name='recipe_c'),
    path('recipe/<int:id>/', views.RecipeRetrieveView.as_view(), name='recipe_g'),
    path('recipe/<int:id>/update/', views.RecipeUpdateView.as_view(), name='recipe_u'),

    path('ingredient/', views.IngredientListView.as_view(), name='ingredient'),
    path('ingredient/create/', views.IngredientCreateView.as_view(), name='ingredient_c'),
    path('ingredient/<int:id>/', views.IngredientRetrieveView.as_view(), name='ingredient_g'),
    path('ingredient/<int:id>/update/', views.IngredientUpdateView.as_view(), name='ingredient_u'),

    path('process/', views.ProcessListView.as_view(), name='process'),
    path('process/create/', views.ProcessCreateView.as_view(), name='process_c'),
    path('process/<int:id>/', views.ProcessRetrieveView.as_view(), name='process_g'),
    path('process/<int:id>/update/', views.ProcessUpdateView.as_view(), name='process_u'), 
]