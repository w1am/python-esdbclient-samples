from esdbclient import EventStoreDBClient, NewEvent, StreamState
from uuid import uuid4

def run():
    # region createClient
    client = EventStoreDBClient(
        uri="{connectionString}"
    )
    # endregion createClient

    # region createEvent
    event_data = NewEvent(
        id=uuid4(),
        type='TestEvent',
        data=b'I wrote my first event'
    )

    # endregion createEvent

    # region appendEvents
    client.append_to_stream(
        stream_name="some-stream",
        events=event_data
    )
    # endregion appendEvents

    # region readStream
    events = client.get_stream(
        stream_name="some-stream",
        limit=10
    )

    for event in events:
        # Doing something productive with the event
        print(event)
    # endregion readStream