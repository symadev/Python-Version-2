from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    city: str
    zip: int

class User(BaseModel):
    name: str
    addresses: List[Address]

data = {
    "name": "Rahim",
    "addresses": [
        {"city": "Dhaka", "zip": 1207},
        {"city": "Chittagong", "zip": 4000}
    ]
}

user = User(**data)
print(user)



# from pydantic import BaseModel
#
# class User(BaseModel):
#     id: int
#     name: str
#     age: int
#
# # ✅ সঠিক ডেটা
# u1 = User(id=1, name="Rahim", age=23)
# print(u1)
# #
# # # ❌ ভুল ডেটা (age string দেওয়া হয়েছে)
# # u2 = User(id=2, name="Karim", age="twenty")



#
# from pydantic import BaseModel, Field
#
# class Product(BaseModel):
#     name: str = Field(..., min_length=3, max_length=50)
#     price: float = Field(..., gt=0)   # price অবশ্যই 0 এর বেশি হতে হবে
#     stock: int = Field(..., ge=0)     # stock negative হতে পারবে না
#
# # ✅ সঠিক ডেটা
# p1 = Product(name="Laptop", price=50000.0, stock=10)
# print(p1)
#
# # ❌ ভুল ডেটা (price negative)
# p2 = Product(name="TV", price=-20000, stock=5)




# //email--validation
# from pydantic import BaseModel, EmailStr
#
# class User(BaseModel):
#     name: str
#     email: EmailStr
#
# # ✅ সঠিক
# u1 = User(name="Rahim", email="rahim@example.com")
# print(u1)
# #
# # # ❌ ভুল (invalid email)
# # u2 = User(name="Karim", email="not-an-email")
#



# //nested models
from pydantic import BaseModel
from typing import List

class Addresses(BaseModel):
    city: str
    zip: int

class User(BaseModel):
    name: str
    addresses: List[Address]

data = {
    "name": "Rahim",
    "addresses": [
        {"city": "Dhaka", "zip": 1207},
        {"city": "Chittagong", "zip": 4000}
    ]
}

user = User(**data)
print(user)




# Default Values + Optional Field
#
# from pydantic import BaseModel
# from typing import Optional
#
# class User(BaseModel):
#     name: str
#     age: Optional[int] = None   # age না দিলেও চলবে
#     is_active: bool = True      # default value
#
# # ✅ ডেটা age ছাড়া
# u1 = User(name="Rahim")
# print(u1)
#
# # ✅ সব ফিল্ডসহ
# u2 = User(name="Karim", age=30, is_active=False)
# print(u2)


# Custom Validation (Validator Function)
#
# from pydantic import BaseModel, validator
#
# class User(BaseModel):
#     name: str
#     age: int
#
#     @validator("age")
#     def check_age(cls, value):
#         if value < 18:
#             raise ValueError("Age must be at least 18")
#         return value
#
# # ✅ Valid
# u1 = User(name="Rahim", age=25)
# print(u1)
#
# # ❌ Invalid
# u2 = User(name="Karim", age=15)





