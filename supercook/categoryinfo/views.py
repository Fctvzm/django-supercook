from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from recipeinfo.models import Category
from recipeinfo.serializers import CategorySerializer

@csrf_exempt
def category_list(request):
	categories = Category.objects.all()
	ser = CategorySerializer(categories, many = True)
	return JsonResponse(ser.data, safe = False)
