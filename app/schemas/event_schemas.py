from  pydantic import BaseModel, Field
from .examples import ExampleEvent
from datetime import datetime, time as t
from utils.enums import EventStatus



class BaseEvent(BaseModel):
    title: str = Field(examples=[ExampleEvent.title])
    description: str = Field(examples=[ExampleEvent.description])
    category: str = Field(examples=[ExampleEvent.category])
    start_date: datetime = Field(examples=[ExampleEvent.start_date])
    end_date: datetime = Field(examples=[ExampleEvent.end_date])
    time: t = Field(examples=[ExampleEvent.time])
    ticked_price: int = Field(examples=[ExampleEvent.ticked_price])
    ticked_count: int = Field(examples=[ExampleEvent.ticked_count])
    location: str = Field(examples=[ExampleEvent.location])


class EventRequestSchema(BaseEvent):
    pass


class EventResponseSchema(BaseEvent):
    id: int = Field(examples=[ExampleEvent.id])
    organizer_id: int = Field(examples=[ExampleEvent.organizer_id])

    created_at: datetime = Field(examples=[ExampleEvent.created_at])
    status: EventStatus = Field(examples=[ExampleEvent.status])



class EventEditRequestSchema(BaseEvent):
    status: EventStatus = Field(examples=[ExampleEvent.status])







