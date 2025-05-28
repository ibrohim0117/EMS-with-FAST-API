"""Define the Event manager."""

from fastapi import HTTPException, status
from collections.abc import Sequence
from models import Event
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.event_schemas import EventRequestSchema, EventResponseSchema
from database.helpers import EventDB




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


    @staticmethod
    async def get_all_events(session: AsyncSession) -> Sequence[Event]:
        """Get all Events."""
        return await EventDB.all(session)


    @staticmethod
    async def get_event_by_id(event_id: int, session: AsyncSession) -> EventResponseSchema:
        """Return one event by ID."""
        # print(event_id, type(event_id))
        # event = await session.get(Event, event_id)
        event = await EventDB.get(session=session, event_id=event_id)
        if event is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f'Event {event_id} not found')

        return event
