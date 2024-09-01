Reference:

from .auth import ApiKeyAuthentication, ApiKeyPlan

class ApiKeyInfoView(APIView, ApiKeyPlan):
    authentication_classes = [ApiKeyAuthentication]

    def get(self, request):
        plan = self.get_user_plan(request)
        return Response(plan)
