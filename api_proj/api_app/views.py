from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Article
from .api.serializers import ArticleSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser



@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        data = Article.objects.all()
        serializer = ArticleSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)