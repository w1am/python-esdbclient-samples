from esdbclient import EventStoreDBClient

def subscribe_to_stream(client: EventStoreDBClient):
    # region subscribe-to-stream
    subscription = client.subscribe_to_stream(
        stream_name="some-stream"
    )

    for event in subscription:
        # handles the event...

        break

    # endregion subscribe-to-stream

    # region subscribe-to-stream-from-position
    client.subscribe_to_stream(
        stream_name="some-stream",
        stream_position=20
    )
    # endregion subscribe-to-stream-from-position

    # region subscribe-to-stream-live
    client.subscribe_to_stream(
        stream_name="some-stream",
        stream_position=-1, #! how to get END
    )
    # endregion subscribe-to-stream-live

    # region subscribe-to-stream-resolving-linktos
    client.subscribe_to_stream(
        stream_name="$et-myEventType",
        stream_position=0,
        resolve_link_tos=True #! argument does not exist
    )
    # endregion subscribe-to-stream-resolving-linktos

    # region subscribe-to-stream-subscription-dropped
    subscription = client.subscribe_to_stream(
        stream_name="some-stream",
        stream_position=0
    )

    for event in subscription:
        # handles the event...

        #! How to handle subscription dropped?

        break

    # endregion subscribe-to-stream-subscription-dropped


def subscribe_to_all(client: EventStoreDBClient):
    # region subscribe-to-all
    subscription = client.subscribe_to_all()

    for event in subscription:
        # handles the event...

        # handle event appeared and subscription dropped

        break

    # endregion subscribe-to-all

    # region subscribe-to-all-from-position
    client.subscribe_to_all(
        commit_position=1_056,
        prepare_position=1_056 #! prepare position argument does not exist
    )
    # endregion subscribe-to-all-from-position

    # region subscribe-to-all-live
    client.subscribe_to_all(
        stream_position=-1 # how to get END
    )
    # endregion subscribe-to-all-live

    # region subscribe-to-all-subscription-dropped
    subscription = client.subscribe_to_all(
        stream_position=0,
    )

    for event in subscription:
        # handles the event...

        # How to handle subscription dropped?

        break 
    # endregion subscribe-to-all-subscription-dropped


def subscribe_to_filtered(client: EventStoreDBClient):
    # region stream-prefix-filtered-subscription
    client.subscribe_to_all(
        filter_include=["test-*"]
    )
    # endregion stream-prefix-filtered-subscription
    # region stream-regex-filtered-subscription
    client.subscribe_to_all(
        filter_include=["/invoice-\\d\\d\\d/g"]
    )
    # endregion stream-regex-filtered-subscription

def subscribe_to_all_overriding_user_credentials(client: EventStoreDBClient):
    # region overriding-user-credentials
    credentials = client.construct_call_credentials(
        username='admin',
        password='changeit'
    )

    client.subscribe_to_all(
        credentials=credentials
    )
    # endregion overriding-user-credentials