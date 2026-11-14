
from decimal import Decimal
from typing import Annotated

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    StringConstraints,
    model_validator
)


CategoryTitle = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=1,
        max_length=100
    )
]

BookTitle = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True,
        min_length=1,
        max_length=200
    )
]

BookDescription = Annotated[
    str,
    StringConstraints(max_length=5000)
]

PositivePrice = Annotated[
    Decimal,
    Field(gt=0, max_digits=10, decimal_places=2)
]

PositiveId = Annotated[int, Field(gt=0)]


class CategoryBase(BaseModel):
    title: CategoryTitle


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class BookBase(BaseModel):
    title: BookTitle
    description: BookDescription | None = None
    price: PositivePrice
    url: HttpUrl | None = None
    category_id: PositiveId


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: BookTitle | None = None
    description: BookDescription | None = None
    price: PositivePrice | None = None
    url: HttpUrl | None = None
    category_id: PositiveId | None = None

    @model_validator(mode="after")
    def check_required_fields(self):
        for field in ("title", "price", "category_id"):
            if field in self.model_fields_set and getattr(self, field) is None:
                raise ValueError(f"Поле {field} не может быть null")

        return self


class BookResponse(BaseModel):
    id: int
    title: BookTitle
    description: BookDescription | None
    price: Decimal
    url: str | None
    category_id: PositiveId

    model_config = ConfigDict(from_attributes=True)
