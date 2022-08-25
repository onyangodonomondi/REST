from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'price': request.data.get('price'),
            'description': request.data.get('description')
        }
        serializer = DrinkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])

def drink_detail(request, id):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return JsonResponse({'error': 'Drink not found'}, status=404)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = {
            'name': request.data.get('name'),
            'price': request.data.get('price'),
            'description': request.data.get('description')
        }
        serializer = DrinkSerializer(instance=drink, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        drink.delete()
        return JsonResponse({}, status=204)