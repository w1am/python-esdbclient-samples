from esdbclient import EventStoreDBClient, NewEvent, StreamState
from uuid import uuid4
import traceback  

def append_to_stream(client: EventStoreDBClient):
    # region append-to-stream
    event_data = NewEvent(
        type='some-event',
        data=b'{"id": "1", "important_data": "some value"}'
    )

    commit_position = client.append_to_stream(
        stream_name="some-stream",
        current_version=StreamState.NO_STREAM,
        events=event_data
    )
    # endregion append-to-stream

    #! In python it returns the commit position. refer to observation doc for more information
    print(commit_position)


def append_with_same_id(client: EventStoreDBClient):
    # region append-duplicate-event
    id = uuid4()
    event = NewEvent(
        id=id,
        type='some-event',
        data=b'{"id": "1", "important_data": "some value"}'
    )

    try:
        client.append_to_stream(
            stream_name="some-stream",
            current_version=StreamState.ANY,
            events=event
        )

        client.append_to_stream(
            stream_name="some-stream",
            current_version=StreamState.ANY,
            events=event
        )
    except Exception as e:
        traceback.print_exc()
        print(e)
    # endregion append-duplicate-event


def append_with_no_stream(client: EventStoreDBClient):
    # region append-with-no-stream
    event = NewEvent(
        type='some-event',
        data=b'{"id": "1", "important_data": "some value"}'
    )

    client.append_to_stream(
        stream_name="same-event-stream",
        current_version=StreamState.NO_STREAM,
        events=event
    )

    event = NewEvent(
        type='some-event',
        data=b'{"id": "2", "important_data": "some other value"}'
    )

    client.append_to_stream(
        stream_name="same-event-stream",
        current_version=StreamState.NO_STREAM,
        events=event
    )
    # endregion append-with-no-stream

def append_with_concurrency_check(client: EventStoreDBClient):
    # region append-with-concurrency-check
    events = client.get_stream(
        stream_name="concurrency-stream",
        backwards=True,
        limit=1
    )

    last_event = events[-1]

    client_one_event = NewEvent(
        type='some-event',
        data=b'{"id": "1", "important_data": "client one"}'
    )

    client.append_to_stream(
        stream_name="concurrency-stream",
        current_version=last_event.stream_position,
        events=client_one_event
    )

    client_two_event = NewEvent(
        type='some-event',
        data=b'{"id": "1", "important_data": "client one"}'
    )

    client.append_to_stream(
        stream_name="concurrency-stream",
        current_version=last_event.stream_position,
        events=client_two_event
    )
    # endregion append-with-concurrency-check


def append_to_stream_overriding_user_credentials(client: EventStoreDBClient):
    event = NewEvent(
        id=id,
        type='some-event',
        data=b'{"id": "1", "important_data": "some value"}'
    )

    # region overriding-user-credentials
    credentials = client.construct_call_credentials(
        username='admin',
        password='changeit'
    )

    commit_position = client.append_to_stream(
        stream_name="some-stream",
        current_version=StreamState.NO_STREAM,
        events=event,
        credentials=credentials,
    )
    # endregion overriding-user-credentials

    print(f"Commit position: {commit_position}")