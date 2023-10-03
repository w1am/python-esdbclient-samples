from esdbclient import EventStoreDBClient
from samples import appending_events, persistent_subscriptions, server_side_filtering

client = EventStoreDBClient(
    uri="esdb://localhost:2113?tls=false"
)

# persistent_subscriptions.connect_to_persistent_subscription_to_stream(client)
# appending_events.append_to_stream(client)
# server_side_filtering.exclude_system_events(client)