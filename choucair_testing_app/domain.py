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


@dataclasses.dataclass
class DeleteProductDomain:
    product_id: str = None
