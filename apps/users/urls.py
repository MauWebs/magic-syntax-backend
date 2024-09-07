from django.urls import path
from .views import MyTokenObtainPairView, RegisterView, UsersView, UserView, UserProfileView

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view()),
    path('register/', RegisterView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('', UsersView.as_view()),
    path('<int:pk>/', UserView.as_view()),
]