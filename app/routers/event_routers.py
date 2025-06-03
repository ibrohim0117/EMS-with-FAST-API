"""Routes for Events listing and control."""

from collections.abc import Sequence
from typing import Optional, Union

from fastapi import APIRouter, Depends, Request, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database.db import get_database
from managers.auth import can_edit_user, is_admin, oauth2_schema, is_organizer
from managers.event_manager import EventManager
from utils.enums import RoleType
from models import User, Event
from schemas.user import UserChangePasswordRequest, UserEditRequest, MyUserResponse, UserResponse
from schemas.event_schemas import EventRequestSchema, EventResponseSchema, EventEditRequestSchema
from watchfiles import awatch

router = APIRouter(tags=["Events"], prefix="/events")


@router.post("/", dependencies=[Depends(oauth2_schema), Depends(is_organizer)],response_model=EventResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_event(request: Request, event_data: EventRequestSchema, db: AsyncSession = Depends(get_database)) -> Event:

    event = await EventManager.create_event(event_data, request.state.user.id, db)
    return event


@router.get("/list/", response_model=Union[EventResponseSchema, list[EventResponseSchema]], status_code=status.HTTP_200_OK)
async def get_events(db: AsyncSession = Depends(get_database), event_id: Optional[int] = None) -> Union[Sequence[Event], Event]:
    """Get the current event's data only."""
    if event_id is None:
        return await EventManager.get_all_events(db)
    return await EventManager.get_event_by_id(session=db, event_id=event_id)



@router.put("/{event_id}", response_model=EventResponseSchema, dependencies=[Depends(oauth2_schema), Depends(is_organizer)])
async def update_event(request: Request, event_id: int, event_data: EventEditRequestSchema, db: AsyncSession = Depends(get_database)) -> Event:
    event = await EventManager.get_event_by_id(session=db, event_id=event_id)
    if event.organizer_id != request.state.user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Is user not in organizer or admin")


















