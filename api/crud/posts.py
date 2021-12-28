from sqlalchemy.engine.base import Engine
from sqlmodel import Session, select

from api.models import PostQL, Post


def get_posts(engine: Engine, slug: str | None) -> list:
    with Session(engine) as session:
        statement = select(Post).where(Post.slug == slug) if slug else select(Post)
        posts = session.exec(statement).all()
    return [
        PostQL(
            slug=post.slug,
            title=post.title,
            content=post.content,
            published=post.published,
            published_at=post.published_at,
        )
        for post in posts
    ]


def create_post(engine: Engine, post: PostQL) -> PostQL:
    with Session(engine) as session:
        session.add(
            Post(
                slug=post.slug,
                title=post.title,
                content=post.content,
                published=post.published,
                published_at=post.published_at,
            )
        )
        session.commit()
    return post
