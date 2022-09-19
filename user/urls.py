from django.urls import path
from .views import Register, Login
from . import views

urlpatterns = [
    path('registration/', Register.as_view(), name='registration'),
    path('login/',Login.as_view(), name='login'),
    # path('login', views.Login.as_view(), name='login_api'),
    path('verify_token/<str:token>', views.VerifyToken.as_view(), name='verify_token_api')
]

