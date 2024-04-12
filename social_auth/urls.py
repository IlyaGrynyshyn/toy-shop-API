from django.urls import path

from social_auth.views import GoogleSocialAuthView, FacebookSocialAuthView

app_name = "social_auth"

urlpatterns = [
    path("google/", GoogleSocialAuthView.as_view(), name="google"),
    path("facebook/", FacebookSocialAuthView.as_view(), name="facebook"),
]
