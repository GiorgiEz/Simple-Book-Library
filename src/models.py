from sqlmodel import Field, SQLModel
from typing import Optional


class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    year: int
    genre: Optional[str] = None
