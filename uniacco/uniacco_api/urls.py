from django.urls import path, include
from uniacco_api.views import reg_user_view, get_user_view, UserLoginView, get_user_login_history_view
from rest_framework import routers


# from uniacco_api.views import UserAPIView


router = routers.DefaultRouter()
urlpatterns = [
    path('register/', reg_user_view, name='register'),
    path('users/', get_user_view, name='users'),
    path('signin/', UserLoginView, name='login'),
    path('userhistory/', get_user_login_history_view, name = 'history' )
    # path('api/user/', UserAPIView.as_view(), name='user'),
]

