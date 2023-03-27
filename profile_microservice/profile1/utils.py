import jwt
from django.conf import settings

def validate_token(access_token):
    try:
        
        # print(access_token)
        payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms=['HS256'])
        # print(payload)
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        raise jwt.InvalidTokenError('Invalid token')
