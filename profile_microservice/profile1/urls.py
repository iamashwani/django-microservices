from django.urls import path
from .views import get_user_profile,create_user_profile

urlpatterns = [
path('user-profile/', get_user_profile, name='get_user_profile'),
path('create-user/', create_user_profile),

]