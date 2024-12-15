from contextlib import asynccontextmanager

from src.config import settings

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

engine = create_async_engine(settings.get_db_urL())
async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)


@asynccontextmanager
async def get_async_session():
    async with async_session_maker() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()

