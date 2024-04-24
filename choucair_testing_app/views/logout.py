from choucair_testing_app.domain import loginDomain
from choucair_testing_app.serializer import LoginSerializer
from choucair_testing_app.use_cases.logout import LogoutUseCase
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        domain = loginDomain(**serializer.data)
        uc = LogoutUseCase()
        return uc.execute(domain=domain, request=request)
