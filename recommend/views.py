from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from .serializers import UserSerializer
# from .models import User
# from rest_framework import generics
# from rest_framework.parsers import JSONParser


@csrf_exempt
def nutrition(request):
    # 재료 기입
    if request.method == 'POST':
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


@csrf_exempt
def like(request):
    # 재료 기입
    if request.method == 'POST':
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


@csrf_exempt
def nutrition_result(request):
    # 영양소 균형 기준 메뉴 내보내기
    if request.method == 'GET':
        return HttpResponse(status=200)
    # 좋아요 점수 가져오기
    elif request.method == 'POST':
        return HttpResponse(status=201)
    else:
        return HttpResponse(status=400)


@csrf_exempt
def like_result(request):
    # 선호도 기준 메뉴 내보내기
    if request.method == 'GET':
        return HttpResponse(status=200)
    # 좋아요 점수 가져오기
    elif request.method == 'POST':
        return HttpResponse(status=201)
    else:
        return HttpResponse(status=400)
