from choucair_testing_app.domain import loginDomain
from django.contrib.auth import authenticate, logout
from rest_framework.views import Response
from rest_framework import status
from rest_framework.authtoken.models import Token


class LogoutUseCase:
    def execute(self, domain: loginDomain, request):
        try:
            username = domain.username
            password = domain.password
            # get the token of the headers
            token = request.headers.get("Authorization").split(" ")[1]
            # validate the user's existence
            user = authenticate(username=username, password=password)
            if user:
                # Logout session
                logout(request)
                # Delete session token
                Token.objects.filter(key=token).delete()
                return Response(
                    {"Mesage": "The logout was successful"},
                    status.HTTP_200_OK
                )
            return Response(
                {"Message": "The user does not exist"},
                status.HTTP_403_FORBIDDEN
            )
        except Exception as error:
            return Response(
                data=error.args,
                status=status.HTTP_400_BAD_REQUEST,
                content_type="application/json"
            )
