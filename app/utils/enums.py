# pylint: disable=invalid-name
"""Define Enums for this project."""

from enum import Enum


class RoleType(Enum):
    """Contains the different Role types Users can have."""
    user = "user"
    admin = "admin"
    organizer = "organizer"


class EventStatus(Enum):
    not_started = "not_started"
    counting = "counting"
    finished = "finished"
    cancelled = "cancelled"


class TickedStatus(Enum):
    available = "available"
    not_available = "not_available"


class PaymentMethod(Enum):
    cash = "cash"
    card = "card"


class PaymentStatus(Enum):
    pending = "pending"
    approved = "approved"
    declined = "declined"
    out_of_balance = "out_of_balance"
