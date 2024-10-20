from django.urls import path
from .views import index, other_page, BBLoginView, BBLogoutView, profile

app_name = 'main'
urlpatterns = [
    path("accounts/login/", BBLoginView.as_view(), name="login"),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
    path("accounts/profile/", profile, name="profile"),
    path("accounts/logout/", BBLogoutView.as_view(), name="logout")
]
