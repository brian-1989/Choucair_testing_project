from django.urls import path
from choucair_testing_app.views.login import LoginView
from choucair_testing_app.views.user_register import UserRegisterView
from choucair_testing_app.views.logout import LogoutView
from choucair_testing_app.views.product import (
    GetProductView,
    CreateProductView,
    UpdateproductView,
    DeleteProductView
)

urlpatterns = [

]

urlpatterns += [
    path('login/', LoginView.as_view(), name='login'),
    path('user_register/', UserRegisterView.as_view(), name='user_register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('get_product/', GetProductView.as_view(), name='get_product'),
    path('create_product/', CreateProductView.as_view(), name='create_product'),
    path('update_product/', UpdateproductView.as_view(), name='update_product'),
    path('delete_product/', DeleteProductView.as_view(), name='delete_product')
]