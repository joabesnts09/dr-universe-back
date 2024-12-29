from django.urls import path
from accounts.views import AccountView
from rest_framework_simplejwt import views


urlpatterns = [
    path('accounts/', AccountView.as_view(), name='create_account'),
    path('login/', views.TokenObtainPairView.as_view(), name='login'),
    path('refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
]