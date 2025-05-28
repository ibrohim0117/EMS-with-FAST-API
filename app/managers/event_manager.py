"""Define the Event manager."""

from fastapi import HTTPException, status
from passlib.context import CryptContext
from models import Event
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.event_schemas import EventRequestSchema, EventResponseSchema

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



class EventManager:
    """Class to Manage the Event."""

    @staticmethod
    async def create_event(event_data: EventRequestSchema, organizer_id: int, session: AsyncSession) -> EventResponseSchema:
        """Create a new event."""
        try:
            new_event_data = event_data.model_dump()
            new_event_data["organizer_id"] = organizer_id
            event = Event(**new_event_data)
            session.add(event)
            await session.flush()
            await session.refresh(event)
            print(event, type(event))

            return event

        except Exception as err:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Xatolik {err}') from err
