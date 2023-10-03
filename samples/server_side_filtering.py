from esdbclient import EventStoreDBClient, ESDB_SYSTEM_EVENTS_REGEX

def exclude_system_events(client: EventStoreDBClient):
    # region exclude-system
    subscription = client.subscribe_to_all(
        filter_exclude=[ESDB_SYSTEM_EVENTS_REGEX]
    )
    
    for event in subscription:
        #! Get the stream id 
        #! Get the revision 

        print(f"received event: {event.stream_position} {event.type}")

    # endregion exclude-system


def event_type_prefix(client: EventStoreDBClient):
    # region event-type-prefix
    subscription = client.subscribe_to_all(
        filter_exclude=["customer-*"]
    )

    for event in subscription:
        #! Get the stream id 
        #! Get the revision 

        print(f"Event: {event}")
    # endregion event-type-prefix


def event_type_regex(client: EventStoreDBClient):
    # region event-type-regex
    subscription = client.subscribe_to_all(
        filter_include=["^user|^company"]
    )

    for event in subscription:
        #! Get the stream id 
        #! Get the revision 

        print(f"Event: {event}")
    # endregion event-type-regex


def stream_prefix(client: EventStoreDBClient):
    # region stream-prefix
    subscription = client.subscribe_to_all(
        filter_by_stream_name=True,
        filter_include=["user-*"]
    )
    for event in subscription:
        #! Get the stream id 
        #! Get the revision 

        print(f"Event: {event}")
    # endregion stream-prefix


def stream_regex(client: EventStoreDBClient):
    # region stream-regex
    subscription = client.subscribe_to_all(
        filter_by_stream_name=True,
        filter_include=["^account|^savings"]
    )
    for event in subscription:
        #! Get the stream id 
        #! Get the revision 

        print(f"Event: {event}")
    # endregion stream-regex


def checkpoint_callback_with_interval(client: EventStoreDBClient):
    # region checkpoint-with-interval
    subscription = client.subscribe_to_all(
        include_checkpoints=["/^[^\\$].*/"]
    )
    # endregion checkpoint-with-interval

    # region checkpoint
    for event in subscription:
        #! Get the stream id 
        #! Get the revision 

        print(f"Event: {event}")
    # endregion checkpoint