# views.py in profile_microservice

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from .serializers import UserProfileSerializer
from .utils import validate_token

@api_view(['GET'])

def get_user_profile(request):
    access_token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
    

    user_id = validate_token(access_token)
    if user_id is None:
        return Response({'error': 'Invalid access token'}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        profile = UserProfile.objects.get(user_id=user_id)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)
    except UserProfile.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_user_profile(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)