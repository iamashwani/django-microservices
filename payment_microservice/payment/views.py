# views.py in payment_microservice

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer
from .utils import validate_token

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def make_payment(request):
    access_token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
    user_id = validate_token(access_token)
    if user_id is None:
        return Response({'error': 'Invalid access token'}, status=status.HTTP_401_UNAUTHORIZED)
    amount = request.data.get('amount', None)
    if amount is None:
        return Response({'error': 'Amount not provided'}, status=status.HTTP_400_BAD_REQUEST)
    payment = Payment(user_id=user_id, amount=amount)
    payment.save()
    serializer = PaymentSerializer(payment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
