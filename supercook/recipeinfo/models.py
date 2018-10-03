from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
	name = models.CharField(max_length = 100, unique = True)
	UNITS_CHOICES = (
		('g', 'gramm'),
		('tbsp', 'tablespoon'),
		('ml', 'mililiter'),
		('l', 'liter'),
		('kg', 'kilogramm'),
		('', '')
	)
	unit = models.CharField(max_length = 10, choices = UNITS_CHOICES, default = '', blank = True, null = True)

	class Meta:
		ordering = ["name"]

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length = 20, unique = True)
	descriptor = models.CharField(max_length = 20, unique = True)
	image = models.ImageField(null = True)

	class Meta:
		ordering = ["name"]

	def __str__(self):
		return self.name

class Recipe(models.Model):
	title = models.CharField(max_length = 100)
	created_at = models.DateTimeField(auto_now = True)
	DIFFICULTY_CHOICES = (
		('Easy', 'Easy'),
		('Meduim', 'Meduim'),
		('Hard', 'Hard')
	)
	difficulty = models.CharField(max_length = 10, choices = DIFFICULTY_CHOICES, default = 'Easy')
	ingredients = models.ManyToManyField(Ingredient, through = "Shoplist")
	image = models.ImageField(null = True)
	likes = models.IntegerField(default = 0)
	servings = models.IntegerField(default = 12)
	category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True)
	
	def __str__(self):
		return self.title

class Instruction(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
	order = models.IntegerField()
	text = models.TextField()
	image = models.ImageField(null = True)

	class Meta:
		unique_together = ('recipe', 'image')
		ordering = ["order"]
	
	def __str__(self):
		return self.recipe.title + "___" + "order_" + str(self.order)

class Shoplist(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
	ingredient = models.ForeignKey(Ingredient, on_delete = models.CASCADE)
	amount = models.FloatField(null = True, blank = True)

	def __str__(self):
		return self.recipe.title + "___" + self.ingredient.name

	class Meta:
		unique_together = ('recipe', 'ingredient')


class Review(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	text = models.TextField()

	def __str__(self):
		return self.recipe.title + "___" + self.user.username


	
	
