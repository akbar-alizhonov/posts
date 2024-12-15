from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src import Post
from src.database import get_async_session
from src.post.schema import PostSchema

router = APIRouter(prefix="/post", tags=["Post"])


@router.get("/{post_id}")
async def get_message(
        post_id: int,
        session: Annotated[AsyncSession, Depends(get_async_session)]
):
    post = await session.get(Post, post_id)
    return post


@router.post("/create-post")
async def create_post(
        post_data: Annotated[PostSchema, Depends()],
        session: Annotated[AsyncSession, Depends(get_async_session)]
):
    post = Post(
        title=post_data.title,
        description=post_data.description
    )

    session.add(post)
    await session.commit()
    await session.flush()

    return post