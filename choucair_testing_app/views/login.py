from choucair_testing_app.domain import loginDomain
from choucair_testing_app.serializer import LoginSerializer
from choucair_testing_app.use_cases.login import LoginUseCase
from rest_framework.views import APIView
from rest_framework.request import Request


class LoginView(APIView):
    # Exclude authentication and permissions
    authentication_classes = []
    permission_classes = []

    def post(self, request: Request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        domain = loginDomain(**serializer.data)
        uc = LoginUseCase()
        return uc.execute(domain=domain, request=request)
