from esdbclient import EventStoreDBClient, NewEvent, StreamState, exceptions
from uuid import uuid4

def read_from_stream(client: EventStoreDBClient):
    # region read-from-stream
    events = client.get_stream(
        stream_name="some-stream",
        backwards=False,
        stream_position=0, #! must confirm if stream position and from are the same thing. if it is, then, it is better to use stream position
        limit=100
    )

    # endregion read-from-stream

    # region iterate-stream
    for event in events:
        # Doing something productive with the event
        print(f"Event: {event}")
    # endregion iterate-stream


def read_from_stream_position(client: EventStoreDBClient):
    # region read-from-stream-position
    events = client.get_stream(
        stream_name="some-stream",
        stream_position=10,
        limit=20
    )
    # endregion read-from-stream-position

    # region iterate-stream
    for event in events:
        print(f"Event: {event}")
    # endregion iterate-stream


def read_stream_overriding_user_credentials(client: EventStoreDBClient):
    # region overriding-user-credentials
    credentials = client.construct_call_credentials(
        username='admin',
        password='changeit'
    )

    stream = client.read_stream(
        stream_position=0,
        credentials=credentials
    )
    # endregion overriding-user-credentials


def read_from_stream_position_check(client: EventStoreDBClient):
    # region checking-for-stream-presence
    events = client.get_stream(
        stream_name="some-stream",
        backwards=False, 
        stream_position=10,
        limit=100
    )

    try :
        for event in events:
            print(event.data)
    except Exception as e: 
        if exceptions.NotFound:
            print("Stream not found")
            return
        
        raise e
    # endregion checking-for-stream-presence


def read_stream_backwards(client: EventStoreDBClient):
    # region reading-backwards
    events = client.get_stream(
        stream_name="some-stream",
        backwards=True,
        stream_position=-1, #! Is it better to use -1 or Enums.StreamState.END like in the C# and Go client?
        limit=10
    )

    for event in events:
        print(f"Event: {event}")
    # endregion reading-backwards


def read_from_all_stream(client: EventStoreDBClient):
    # region read-from-all-stream
    stream = client.read_all(
        commit_position=0,
        backwards=False,
        limit=100
    )
    # endregion read-from-all-stream
    # region read-from-all-stream-iterate
    events = tuple(stream)

    for event in events:
        print(f"Event: {event}")
    # endregion read-from-all-stream-iterate


def ignore_system_events(client: EventStoreDBClient):
    # region ignore-system-events
    stream = client.read_all(
        limit=100
    )

    events = tuple(stream)

    for event in events:
        if event.event_type.startswith('$'):
            continue

        print(f"Event: {event}")
    # endregion ignore-system-events


def read_from_all_backwards(client: EventStoreDBClient):
    # region read-from-all-stream-backwards
    stream = client.read_all(
        backwards=True,
        commit_position=-1, #! How to read end
        limit=100
    )
    # endregion read-from-all-stream-backwards
    # region read-from-all-stream-backwards-iterate
    events = tuple(stream)

    for event in events:
        print(f"Event: {event}")
    # endregion read-from-all-stream-backwards-iterate


def read_from_stream_resolving_link_to_s(client: EventStoreDBClient):
    # region read-from-all-stream-resolving-link-Tos
    client.read_all(
        resolve_link_tos=True, #! this does not exist
        limit=100
    )
    # endregion read-from-all-stream-resolving-link-Tos


def read_all_overriding_user_credentials(client: EventStoreDBClient):
    # region read-all-overriding-user-credentials
    credentials = client.construct_call_credentials(
        username='admin',
        password='changeit'
    )

    client.read_all(
        commit_position=0,
        credentials=credentials
    )
    # endregion read-all-overriding-user-credentials