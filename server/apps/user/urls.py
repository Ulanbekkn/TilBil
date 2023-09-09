from django.urls import path
from server.apps.user.views import *

urlpatterns = [
    path('', UserListView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('register/', RegisterUser.as_view()),
]
