from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from .serializers import UserSerializer
# from .models import User
# from rest_framework import generics
# from rest_framework.parsers import JSONParser


@csrf_exempt
def nutrition(request):
    if request.method == 'POST':
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


@csrf_exempt
def like(request):
    if request.method == 'POST':
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


@csrf_exempt
def nutrition_result(request):
    if request.method == 'GET':
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


@csrf_exempt
def like_result(request):
    if request.method == 'GET':
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)
