from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from .models import ApiKey


class ApiKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        if not auth_header.startswith('Bearer '):
            raise AuthenticationFailed('Invalid token header. No credentials provided.')

        api_key = auth_header.split(' ')[1]

        if len(api_key) != 43:
            raise AuthenticationFailed('Invalid API Key length')

        try:
            api_key_obj = ApiKey.objects.get(key=api_key)
        except ApiKey.DoesNotExist:
            raise AuthenticationFailed('Invalid API Key')

        user = api_key_obj.user

        self.user_plan = user.plan if user else None

        return (user, None)


class ApiKeyPlan:
    def get_user_plan(self, request):
        auth = ApiKeyAuthentication()
        auth.authenticate(request)
        if not auth.user_plan:
            raise AuthenticationFailed('User not found or plan not available')
        return str(auth.user_plan)

    def get_allowed_plans(self, user_plan):
        if user_plan == 'free':
            return ['free']
        elif user_plan == 'basic':
            return ['free', 'basic']
        elif user_plan == 'expert':
            return ['free', 'basic', 'expert']
        else:
            return []
