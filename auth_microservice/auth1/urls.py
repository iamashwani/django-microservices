from django.urls import path
from .views import ObtainTokenView, RegisterView

urlpatterns = [
    path('auth/token/', ObtainTokenView.as_view()),
    path('auth/register/', RegisterView.as_view()),
]