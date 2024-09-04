from Design_Patterns.Behavioral_Patterns.Observer.EventListener import EventListener


class EmailNotificationListener(EventListener):
    def __init__(self, email):
        self.email = email

    def update(self, event_type, file):
        print(f"Email to {self.email}: Someone has performed {event_type} operation on file {file}")
