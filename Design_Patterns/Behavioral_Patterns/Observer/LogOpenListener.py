from Design_Patterns.Behavioral_Patterns.Observer.EventListener import EventListener


class LogOpenListener(EventListener):
    def __init__(self, log_file):
        self.log_file = log_file

    def update(self, event_type, file):
        print(f"Save log to {self.log_file}: Some one has performed {event_type} operation on file {file}")
