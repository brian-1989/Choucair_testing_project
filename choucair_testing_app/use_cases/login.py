from choucair_testing_app.domain import loginDomain
from django.contrib.auth import authenticate, login
from django.db.utils import IntegrityError
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import Response


class LoginUseCase:
    def execute(self, domain: loginDomain, request):
        try:
            username = domain.username
            password = domain.password
            # validate the user's existence
            user = authenticate(username=username, password=password)
            if user:
                # Session begins
                login(request, user)
                # Assigning the token to the user
                token = Token.objects.create(user=user)
                token.save()
                return Response(
                    {"Token": str(token)}, status.HTTP_201_CREATED)
            return Response(
                {"Message": "The user does not exist"}, status.HTTP_403_FORBIDDEN)
        # This exception is triggered when the user has already been assigned a token,
        # then it is deleted and a new token is assigned.
        except IntegrityError as error:
            Token.objects.filter(user=user).delete()
            new_token = Token.objects.create(user=user)
            new_token.save()
            return Response({"Token": str(new_token)})
        except Exception as error:
            return Response(
                data=error.args,
                status=status.HTTP_400_BAD_REQUEST,
                content_type="application/json"
            )
