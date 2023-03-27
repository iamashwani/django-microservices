import jwt
from django.conf import settings

def validate_token(access_token):
    try:
        payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None