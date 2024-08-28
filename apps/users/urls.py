from django.urls import path
from .views import MyTokenObtainPairView, RegisterViews, UsersViews, UserViews

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view()),
    path('register/', RegisterViews.as_view()),
    path('', UsersViews.as_view()),
    path('<int:pk>/', UserViews.as_view()),
]
