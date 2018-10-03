from django.urls import path
from . import views

urlpatterns = [
	path('', views.recipe_list, name = 'recipe_list'),
	path('<int:recipe_id>', views.recipe_info, name = 'recipe_info'),
	path('add_review', views.review_add, name = 'review_add')
]