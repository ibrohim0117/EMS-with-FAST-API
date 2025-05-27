"""Define the Users model."""

from sqlalchemy import (
    Boolean, Enum, String, TEXT, Date, Time, DateTime,
    Float, Integer, ForeignKey
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date, time as t, datetime

from database.db import Base
from utils.enums import (
    RoleType, EventStatus, TickedStatus,
    PaymentMethod, PaymentStatus
)


class User(Base):
    """Define the Users model."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    password: Mapped[str] = mapped_column(String(255))
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(50))
    role: Mapped[RoleType] = mapped_column(
        Enum(RoleType),
        nullable=False,
        server_default=RoleType.user.value,
        index=True,
    )
    banned: Mapped[bool] = mapped_column(Boolean, default=False)
    verified: Mapped[bool] = mapped_column(Boolean, default=False)

    events: Mapped[list["Event"]] = relationship()
    tickets: Mapped[list["Ticket"]] = relationship()
    payments: Mapped[list["Payment"]] = relationship()

    def __repr__(self) -> str:
        """Define the model representation."""
        return f'User({self.id}, "{self.first_name} {self.last_name}")'



class Event(Base):
    """Define the Events model."""

    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    description: Mapped[str] = mapped_column(TEXT)
    category: Mapped[str] = mapped_column(String(50), unique=True, index=True)

    start_date: Mapped[date] = mapped_column(Date)
    end_date: Mapped[date] = mapped_column(Date)
    time: Mapped[t] = mapped_column(Time)

    ticked_price: Mapped[float] = mapped_column(Float)
    ticked_count: Mapped[int] = mapped_column(Integer)

    location: Mapped[str] = mapped_column(String(150))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    status: Mapped[EventStatus] = mapped_column(
        Enum(EventStatus),
        nullable=False,
        server_default=EventStatus.not_started.value,
        index=True,
    )

    organizer_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    organizer: Mapped[User] = relationship("User", back_populates="events")

    tickets: Mapped[list["Ticket"]] = relationship()


    def __repr__(self) -> str:
        """Define the model representation."""
        return f'Event({self.id}, "{self.title}")'


class Ticket(Base):
    """Define the Tickets model."""

    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[TickedStatus] = mapped_column(
        Enum(TickedStatus),
        nullable=False,
        server_default=TickedStatus.not_available.value,
        index=True,
    )

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship("User", back_populates="tickets")

    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))
    event: Mapped[Event] = relationship("Event", back_populates="tickets")

    payments: Mapped[list["Payment"]] = relationship()


    def __repr__(self) -> str:
        """Define the model representation."""
        return f'Ticked({self.id}, "{self.status}")'


class Payment(Base):
    """Define the Payments model."""

    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    payment_method: Mapped[PaymentMethod] = mapped_column(
        Enum(PaymentMethod),
        nullable=False,
        server_default=PaymentMethod.cash.value,
        index=True,
    )
    status: Mapped[PaymentStatus] = mapped_column(
        Enum(PaymentStatus),
        nullable=False,
        server_default=PaymentStatus.pending.value,
        index=True,
    )
    card_number: Mapped[str] = mapped_column(String(16), nullable=True)
    exp_date: Mapped[str] = mapped_column(String(5), nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship("User", back_populates="payments")

    ticket_id: Mapped[int] = mapped_column(ForeignKey("tickets.id"))
    ticket: Mapped[Ticket] = relationship("Ticket", back_populates="payments")

    def __repr__(self) -> str:
        """Define the model representation."""
        return f'Payment ({self.id}, "{self.status}")'








