from django.urls import path
from server.apps.user.views import *

urlpatterns = [
    path('', UserListView.as_view()),
    path('login/', Login.as_view()),
    path('register/', RegisterAPI.as_view()),
]
