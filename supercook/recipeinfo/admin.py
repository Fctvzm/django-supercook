from django.contrib import admin
from recipeinfo.models import Ingredient, Recipe, Shoplist, Review, Instruction, Category

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Shoplist)
admin.site.register(Review)
admin.site.register(Instruction)
admin.site.register(Category)