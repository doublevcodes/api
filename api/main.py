from datetime import datetime
from os import getenv
from typing import Optional

from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from sqlmodel import create_engine, SQLModel

from api.models import PostQL
from api.crud import create_post, get_posts

ENGINE = create_engine(getenv("DATABASE_URL"))


@strawberry.type
class Query:
    @strawberry.field
    def post(self, slug: Optional[str] = None) -> list[PostQL]:
        return get_posts(ENGINE, slug)


@strawberry.type
class Mutation:
    @strawberry.field
    def add_post(self, slug: str, title: str, content: str, published: bool) -> PostQL:
        return create_post(
            ENGINE,
            PostQL(
                slug=slug,
                title=title,
                content=content,
                published=published,
                published_at=datetime.now(),
            ),
        )


schema = strawberry.Schema(query=Query, mutation=Mutation)

SQLModel.metadata.create_all(ENGINE)

graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)
