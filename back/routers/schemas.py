from pydantic.dataclasses import dataclass
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel


@dataclass
class User:
    id: int
    username: str
    first_name: str
    last_name: str
    age: int
    created_at: datetime


class UpdateUserSchema(BaseModel):
    id: Optional[int]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    age: Optional[int]
    created_at: Optional[datetime]

# class UserSchema(BaseModel):
#     id: int
#     username: str
#     first_name: str
#     last_name: str
#     age: int
#     created_at: datetime

#     class Config:
#         schema_extra = {
#             "example": {
#                 "id": 1,
#                 "username": "john12",
#                 "first_name": "John",
#                 "last_name": "Doe",
#                 "age": 3,
#             }
#         }


@dataclass
class UserList:
    count: int
    users: List[User]
