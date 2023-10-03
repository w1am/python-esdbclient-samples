from esdbclient import EventStoreDBClient, RecordedEvent

def create_persistent_subscription(client: EventStoreDBClient):
    # region create-persistent-subscription-to-stream
    client.create_subscription_to_stream(
        stream_name="test-stream",
        group_name="subscription-group"
    )
    # endregion create-persistent-subscription-to-stream

def handle_event(event: RecordedEvent):
    # handle event here
    print(f"Handling event {event.type}")

def connect_to_persistent_subscription_to_stream(client: EventStoreDBClient):
    # region subscribe-to-persistent-subscription-to-stream
    subscription = client.read_subscription_to_stream(
        stream_name="test-stream",
        group_name="subscription-group",
    )

    try:
        for event in subscription:
            try:
                print(f'handling event {event.type} with retryCount {event.retry_count}')
                handle_event(event=event)
                subscription.ack(event_id=event.id)
            except Exception as ex:
                print(f'handling failed with exception {ex}')
                subscription.nack(
                    event_id=event.id,
                    action="park"
                )
    except BaseException as e:
        print(f'Subscription was dropped. {e}')
    # endregion subscribe-to-persistent-subscription-to-stream

def connect_to_persistent_subscription_to_all(client: EventStoreDBClient):
    # region subscribe-to-persistent-subscription-to-all
    subscription = client.read_subscription_to_all(
        group_name="subscription-group"
    )

    try:
        for event in subscription:
            try:
                print(f'handling event {event.type} with retryCount {event.retry_count}')

                # handle event here

                subscription.ack(event_id=event.id)
            except Exception as ex:
                print(f'handling failed with exception {ex}')
                subscription.nack(
                    event_id=event.id,
                    action="park"
                )
    except BaseException as e:
        print(f'Subscription was dropped. {e}')

    # endregion subscribe-to-persistent-subscription-to-all

def create_persistent_subscription_to_all(client: EventStoreDBClient):
    # region create-persistent-subscription-to-all
    client.create_subscription_to_all(
        group_name="subscription-group",
        filter_include=["test*"],
    )
    # endregion create-persistent-subscription-to-all

def connect_to_persistent_subscription_with_manual_acks(client: EventStoreDBClient):
    # region subscribe-to-persistent-subscription-with-manual-acks
    subscription = client.read_subscription_to_stream(
        stream_name="test-stream",
        group_name="subscription-group",
    )

    try:
        for event in subscription:
            try:
                print(f'handling event {event.type} with retryCount {event.retry_count}')
                
                # handle event here

                subscription.ack(event_id=event.id)
            except Exception as ex:
                print(f'handling failed with exception {ex}')
                subscription.nack(
                    event_id=event.id,
                    action="park"
                )
    except BaseException as e:
        print(f'Subscription was dropped. {e}')
    # endregion subscribe-to-persistent-subscription-with-manual-acks

def update_persistent_subscription(client: EventStoreDBClient):
    #region update-persistent-subscription
    subscription = client.update_subscription_to_stream(
        stream_name="test-stream",
        group_name="subscription-group",
        #! missing resolveLinkTos and checkPointLowerBound ...
    )
    #endregion update-persistent-subscription

def delete_persistent_subscription(client: EventStoreDBClient):
    client.delete_subscription(
        stream_name="test-stream",
        group_name="subscription-group",
    )