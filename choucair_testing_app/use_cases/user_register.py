from choucair_testing_app.domain import UserRegisterDomain
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from rest_framework.views import Response
from rest_framework import status


class UserRegisterUseCase:
    def execute(self, domain: UserRegisterDomain):
        try:
            # Create user
            User.objects.create_user(**domain.__dict__).save()
            # Get user information
            get_user = User.objects.filter(
                first_name=domain.first_name).values()
            return Response(list(get_user)[0], status.HTTP_201_CREATED)
        # This exception is to notify that the user is already created.
        except IntegrityError as error:
            return Response(
                data={"Message": f"The user '{domain.first_name}' exist"},
                status=status.HTTP_400_BAD_REQUEST,
                content_type="application/json"
            )
        except Exception as error:
            return Response(
                data=error.args,
                status=status.HTTP_400_BAD_REQUEST,
                content_type="application/json"
            )
