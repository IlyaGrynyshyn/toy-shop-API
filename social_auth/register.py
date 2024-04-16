from django.contrib.auth import authenticate, get_user_model
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed


def register_social_user(
    provider: str, email: str, first_name: str, last_name: str
) -> dict | AuthenticationFailed:
    """
    Register a new user by providing.
    :param provider:
    :param email:
    :param name:
    :return:
    """
    get_user_by_email = get_user_model().objects.filter(email=email)

    if get_user_by_email.exists():
        if provider == get_user_by_email.first().auth_provider:
            registered_user = authenticate(
                email=email, password=settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
            )
            return {
                "email": registered_user.email,
                "tokens": registered_user.tokens(),
            }
        else:
            raise AuthenticationFailed(
                detail="Please continue your login using "
                + get_user_by_email.first().auth_provider
            )
    else:
        user = {
            "email": email,
            "password": settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
            "first_name": first_name,
            "last_name": last_name,
        }
        user = get_user_model().objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.save()
        new_user = authenticate(
            email=email, password=settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
        )
        return {
            "email": new_user.email,
            "tokens": new_user.tokens(),
        }
