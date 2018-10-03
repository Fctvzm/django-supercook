from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from recipeinfo.models import Recipe, Review
from recipeinfo.serializers import RecipeSerializer, RecipeInfoSerializer, ReviewSerializer

@csrf_exempt
def recipe_list(request):
	recipes = Recipe.objects.all()
	ser = RecipeSerializer(recipes, many = True)
	return JsonResponse(ser.data, safe = False)

@csrf_exempt
def recipe_info(request, recipe_id):
	try:
		recipe = Recipe.objects.get(pk = recipe_id)
	except Exception as e:
		return JsonResponse({"error": str(e)}, status=404)

	ser = RecipeInfoSerializer(recipe)
	return JsonResponse(ser.data)

@csrf_exempt
def review_add(request):
	if request.method == "POST":
		data = JSONParser().parse(request)
		s er = ReviewSerializer(data = data)
		if ser.is_valid():
			ser.save()
			return JsonResponse(ser.data, status=201)
		return JsonResponse(ser.errors, status=400)



