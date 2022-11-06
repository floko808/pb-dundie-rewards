import json
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, validator

from dundie.database import connect
from dundie.utils.email import check_valid_email


class InvalidEmailError(Exception):
    ...


class Person(BaseModel):
    pk: str
    name: str
    dept: str
    role: str

    @validator("pk")
    def validate_email(cls, v):
        if not check_valid_email(v):
            raise ValueError(f"Invalid email for {v!r}")
        return v

    def __str__(self) -> str:
        return f"{self.name} - {self.role}"


class Balance(BaseModel):
    person: Person
    value: Decimal

    @validator("value", pre=True)
    def value_logic(cls, v):
        return Decimal(v) * 2

    class Config:
        json_encoders = {Person: lambda p: p.pk}


class Movement(BaseModel):
    person: Person
    date: datetime
    actor: str
    value: Decimal


db = connect()

for pk, data in db["people"].items():
    p = Person(pk=pk, **data)

print(type(vars(p)))
print(type(json.dumps(p.dict())))
print(type(p.json()))
print(p.json())


balance = Balance(person=p, value=700)
print(type(balance.dict()))
print(type(balance.json()))
print(balance.json(models_as_dict=False))
