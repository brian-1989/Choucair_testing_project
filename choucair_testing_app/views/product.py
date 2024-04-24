from choucair_testing_app.domain import (
    CreateAndUpdateProductDomain,
    GetProductDomain,
    DeleteProductDomain
)
from choucair_testing_app.use_cases.product import (
    CreateProductUseCase,
    GetProductUseCase,
    UpdateproductUseCase,
    DeleteProductUseCase
)
from choucair_testing_app.serializer import (
    CreateProductSerializer,
    UpdateproductSerializer,
    GetProductSerializer,
    DeleteProductSerializer
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView

class GetProductView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        product_name = request.query_params.get('product_id')
        serializer = GetProductSerializer(data={"product_id": product_name})
        serializer.is_valid(raise_exception=True)
        domain = GetProductDomain(**serializer.data)
        uc = GetProductUseCase()
        return uc.execute(domain=domain)


class CreateProductView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        serializer = CreateProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Process for adding the product name to the image name
        change_image_name = serializer.validated_data
        image = change_image_name["product_image"]
        product_name = change_image_name["product_name"]
        image.name = f"{product_name}.png"
        change_image_name["product_image"] = image

        domain = CreateAndUpdateProductDomain(**serializer.validated_data)
        uc = CreateProductUseCase()
        return uc.execute(domain=domain)

class UpdateproductView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request: Request):
        serializer = UpdateproductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Process for adding the product name to the image name
        change_image_name = serializer.validated_data
        image = change_image_name["product_image"]
        product_name = change_image_name["product_name"]
        image.name = f"{product_name}.png"
        change_image_name["product_image"] = image

        domain = CreateAndUpdateProductDomain(**serializer.validated_data)
        uc = UpdateproductUseCase()
        return uc.execute(domain=domain)

class DeleteProductView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request: Request):
        product_id = request.query_params.get('product_id')
        serializer = DeleteProductSerializer(data={"product_id": product_id})
        serializer.is_valid(raise_exception=True)
        domain = DeleteProductDomain(**serializer.data)
        uc = DeleteProductUseCase()
        return uc.execute(domain=domain)
