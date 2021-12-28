from datetime import datetime
from typing import Optional

import strawberry
from sqlmodel import Field, SQLModel


@strawberry.type
class PostQL:
    slug: str
    title: str
    content: str
    published: bool = False
    published_at: Optional[datetime] = None


class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    slug: str
    title: str
    content: str
    published: bool = False
    published_at: Optional[datetime] = None
