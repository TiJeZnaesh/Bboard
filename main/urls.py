from django.urls import path
from .views import index, other_page, BBLoginView, BBLogoutView, profile, ProfileEditView
app_name = 'main'
urlpatterns = [
    path("accounts/login/", BBLoginView.as_view(), name="login"),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
    path("accounts/profile/edit/", ProfileEditView.as_view(), name = "profile_edit"),
    path("accounts/profile/", profile, name="profile"),
    path("accounts/logout/", BBLogoutView.as_view(), name="logout")
]
