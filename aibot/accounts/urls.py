from django.urls import path
from .views import UserDetailView, UserCreateView

urlpatterns = [
    path('userdata/', UserDetailView.as_view(), name='user-detail'),
    path('create-user/', UserCreateView.as_view(), name='user-create'),
]


