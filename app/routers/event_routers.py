"""Routes for Events listing and control."""

from collections.abc import Sequence
from typing import Optional, Union

from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.ext.asyncio import AsyncSession

from database.db import get_database
from managers.auth import can_edit_user, is_admin, oauth2_schema, is_organizer
from managers.event_manager import EventManager
from utils.enums import RoleType
from models import User, Event
from schemas.user import UserChangePasswordRequest, UserEditRequest, MyUserResponse, UserResponse
from schemas.event_schemas import EventRequestSchema, EventResponseSchema

router = APIRouter(tags=["Events"], prefix="/events")


@router.post("/", dependencies=[Depends(oauth2_schema), Depends(is_organizer)],response_model=EventResponseSchema)
async def create_event(request: Request, event_data: EventRequestSchema, db: AsyncSession = Depends(get_database)) -> Event:

    event = await EventManager.create_event(event_data, request.state.user.id, db)
    return event

















