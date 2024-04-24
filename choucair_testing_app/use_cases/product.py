from choucair_testing_app.domain import (
    GetProductDomain,
    DeleteProductDomain
)
from choucair_testing_app.serializer import CreateProductSerializer
from choucair_testing_app.models import Products
from datetime import datetime
from rest_framework.views import Response
from rest_framework import status
import pytz

class GetProductUseCase:
    def execute(self, domain: GetProductDomain):
        try:
            # Check if the product is registered
            product = Products.objects.filter(product_id=domain.product_id).values()
            if len(list(product)) == 0:
                return Response(
                    {"Message": f"the product '{domain.product_id}' does not exit"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            return Response(list(product)[0], status.HTTP_200_OK)
        except Exception as error:
            return Response(
                data=error.args,
                status=status.HTTP_400_BAD_REQUEST,
                content_type="application/json"
            )

class CreateProductUseCase:
    def execute(self, domain):
        try:
            # Check if the product is registered
            product = Products.objects.filter(product_name=domain.product_name)
            if len(list(product)) != 0:
                return Response(
                    {"Message": f"the product '{domain.product_name}' is already created"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            # Add creation date
            create_date = datetime.now(tz=pytz.timezone('America/Bogota')).date()
            setattr(domain, "create_date", create_date)
            product_store = Products(**domain.__dict__)
            product_store.save()
            return Response(
                CreateProductSerializer(product_store).data,
                status=status.HTTP_201_CREATED
            )
        except Exception as error:
            return Response(
                data=error.args,
                status=status.HTTP_400_BAD_REQUEST,
                content_type="application/json"
            )

class UpdateproductUseCase:
    def execute(self, domain):
        try:
            # Check if the product is registered
            product = Products.objects.filter(id=domain.id)
            if len(list(product)) == 0:
                return Response(
                    {"Message": f"the product '{domain.product_name}' does not exist"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            # Add update date
            domain.update_date = datetime.now(tz=pytz.timezone('America/Bogota')).date()
            Products.objects.update(**domain.__dict__)
            return Response(
                Products.objects.filter(id=domain.id).values(),
                status.HTTP_200_OK
            )
        except Exception as error:
            return Response(
                data=error.args,
                status=status.HTTP_400_BAD_REQUEST,
                content_type="application/json"
            )

class DeleteProductUseCase:
    def execute(self, domain: DeleteProductDomain):
        try:
            # Check if the product is registered
            product = Products.objects.filter(id=domain.product_id)
            if len(list(product)) == 0:
                return Response(
                    {"Message": f"the product id '{domain.product_id}' does not exist"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            product.delete()
            return Response(
                {"Message": f"The product '{domain.product_id}' was deleted correctly'"},
                status.HTTP_202_ACCEPTED
            )
        except Exception as error:
            return Response(
                data=error.args,
                status=status.HTTP_400_BAD_REQUEST,
                content_type="application/json"
            )
