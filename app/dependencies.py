from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import SessionFactory


async def get_db_session() -> AsyncIterator[AsyncSession]:
    async with SessionFactory() as session:
        yield session
