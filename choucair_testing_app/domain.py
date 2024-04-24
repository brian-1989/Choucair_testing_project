import dataclasses


@dataclasses.dataclass
class loginDomain:
    username: str = None
    password: str = None


@dataclasses.dataclass
class UserRegisterDomain:
    first_name: str = None
    last_name: str = None
    username: str = None
    password: str = None
    email: str = None

class CreateAndUpdateProductDomain:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

@dataclasses.dataclass
class GetProductDomain:
    product_id: str = None

# @dataclasses.dataclass
# class UpdateproductDomain:
#     id: str = None
#     product_name: str = None
#     description: str = None
#     price: int = 0
#     stock: int = 0
#     update_date: str = None

@dataclasses.dataclass
class DeleteProductDomain:
    product_id: str = None
