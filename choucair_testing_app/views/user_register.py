from choucair_testing_app.domain import UserRegisterDomain
from choucair_testing_app.serializer import UserRegisterSerializr
from choucair_testing_app.use_cases.user_register import UserRegisterUseCase
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView

class UserRegisterView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        serializer =  UserRegisterSerializr(data=request.data)
        serializer.is_valid(raise_exception=True)
        domain = UserRegisterDomain(**serializer.data)
        uc = UserRegisterUseCase()
        return uc.execute(domain=domain)

