# Auth.py
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import logging

from .models import ApiKey

logger = logging.getLogger(__name__)


class ApiKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            logger.warning('No Authorization header found')
            return None

        if not auth_header.startswith('Bearer '):
            logger.warning('Invalid token header')
            raise AuthenticationFailed('Invalid token header. No credentials provided.')

        api_key = auth_header.split(' ')[1]

        if len(api_key) != 43:
            logger.warning('Invalid API Key length')
            raise AuthenticationFailed('Invalid API Key length')

        try:
            api_key_obj = ApiKey.objects.get(key=api_key)
        except ApiKey.DoesNotExist:
            logger.warning('Invalid API Key')
            raise AuthenticationFailed('Invalid API Key')

        user = api_key_obj.user
        logger.info('Authentication successful')

        self.user_plan = user.plan if user else None

        return (user, None)


class ApiKeyPlan:
    def get_user_plan(self, request):
        auth = ApiKeyAuthentication()
        auth.authenticate(request)
        if not auth.user_plan:
            raise AuthenticationFailed('User not found or plan not available')
        logger.debug(f'User plan: {auth.user_plan}')
        return str(auth.user_plan)
