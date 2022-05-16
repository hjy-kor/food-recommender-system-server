from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User


class UserListAPI(APIView):
    def get(self, request):
        queryset = User.objects.all()
        print(queryset)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
