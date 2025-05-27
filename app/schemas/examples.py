"""Example data for Schemas."""

from datetime import datetime
from utils.enums import EventStatus

class ExampleUser:
    """Define a dummy user for Schema examples."""

    id = 25
    first_name = "John"
    last_name = "Doe"
    email = "user@example.com"
    password = "My S3cur3 P@ssw0rd"  # noqa: S105
    role = "user"
    banned = False
    verified = True


class ExampleEvent:
    """Define a dummy event for Schema examples."""

    id = 1
    organizer_id = 1
    title = "Hello World konsert"
    description = "Hello World konsert nomli konsert dasturi"
    category = 'Concerts'

    start_date = datetime.now().date()
    end_date = datetime.now().date()
    time = datetime.now().time()

    ticked_price = 10
    ticked_count = 5000

    location = "San Francisco, CA"
    created_at = datetime.now()
    status = EventStatus.not_started













