"""Define the Event manager."""

from fastapi import HTTPException, status, Request
from collections.abc import Sequence
from sqlalchemy import update
from models import Event
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.event_schemas import EventRequestSchema, EventResponseSchema, EventEditRequestSchema
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
            # print(event, type(event))

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



    @staticmethod
    async def update_event(organizer_id: int, event_id: int, event_data: EventEditRequestSchema, session: AsyncSession)->None:
        """Update an event."""

        check_event = await EventDB.get(session, event_id)
        if check_event is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f'Event {event_id} not found')

        if check_event.organizer_id != organizer_id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Is user not in organizer or admin")

        await session.execute(update(Event).where(Event.id == event_id).values(
            title=event_data.title,
            description=event_data.description,
            category=event_data.category,
            start_date=event_data.start_date,
            end_date=event_data.end_date,
            time=event_data.time,
            ticked_price=event_data.ticked_price,
            ticked_count=event_data.ticked_count,
            location=event_data.location,
            status=event_data.status,
        ))

        await session.refresh(check_event)
        return check_event

