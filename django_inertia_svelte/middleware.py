from django.contrib.auth import get_user_model
from inertia import share
from django.conf import settings

User = get_user_model()


class InertiaShare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # share(
        #     request,
        #     user=lambda: request.user,  # evaluated lazily at render time
        # )

        return self.get_response(request)
