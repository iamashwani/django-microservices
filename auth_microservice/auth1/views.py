from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.conf import settings

class ObtainTokenView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.get(username = username)
    
        #user = authenticate(request, username=username, password=password)
        if (user and user.password == password) is None:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        return Response({'access_token': access_token}, status=status.HTTP_200_OK)
    
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create(username=username, password=password, email=email)
        user.save()
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)