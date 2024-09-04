from Design_Patterns.Behavioral_Patterns.Observer.EventListener import EventListener


class EventManager:
    def __init__(self, *operations):
        self.listeners: dict[str, list[EventListener]] = {operation: [] for operation in operations}

    def subscribe(self, event_type, event_listener: EventListener):
        if event_type not in self.listeners:
            raise ValueError(f"Invalid event type: {event_type}")
        self.listeners[event_type].append(event_listener)

    def unsubscribe(self, event_type, event_listener: EventListener):
        if event_listener in self.listeners.get(event_type, []):
            self.listeners[event_type].remove(event_listener)

    def notify(self, event_type, file):
        for event_listener in self.listeners[event_type]:
            event_listener.update(event_type, file)
