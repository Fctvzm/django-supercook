from rest_framework import serializers

from recipeinfo.models import Ingredient, Category, Recipe, Instruction, Shoplist, Review

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('id', 'name', 'image')

class ShoplistSerializer(serializers.HyperlinkedModelSerializer):
	name = serializers.ReadOnlyField(source = 'ingredient.name')
	unit = serializers.ReadOnlyField(source = 'ingredient.unit')
	class Meta:
		model = Shoplist
		fields = ('name', 'unit', 'amount')

class InstructionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Instruction
		fields = ('order', 'text', 'image')

class ReviewInfoSerializer(serializers.ModelSerializer):
	username = serializers.ReadOnlyField(source = 'user.username')
	class Meta:
		model = Review
		fields = ('id', 'username', 'text')

class ReviewSerializer(serializers.Serializer):
	class Meta:
		model = Review
		fields = "__all__"


class RecipeInfoSerializer(serializers.ModelSerializer):
	lists = ShoplistSerializer(source = 'shoplist_set', many = True)
	instructions = InstructionSerializer(source = 'instruction_set', many = True, read_only = True)
	reviews = ReviewInfoSerializer(source = 'review_set', many = True, read_only = True)
	class Meta:
		model = Recipe
		fields = ('id', 'title', 'difficulty', 'lists', 'image', 'likes', 'servings', 'instructions', 'reviews')

class RecipeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Recipe
		fields = ('id', 'title', 'image', 'likes', 'category')



