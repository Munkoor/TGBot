from pydantic import BaseModel


class Book(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True


class CategoryView(BaseModel):
    name: str
    books: list[Book] = []

    class Config:
        orm_mode = True
