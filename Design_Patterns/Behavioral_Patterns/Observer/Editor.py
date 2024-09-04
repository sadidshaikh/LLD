from Design_Patterns.Behavioral_Patterns.Observer.EventManager import EventManager


class Editor:
    def __init__(self):
        self.events: EventManager = EventManager("open", "save")
        self.file = None

    def open_file(self, file_path):
        self.file = file_path
        self.events.notify("open", self.file)

    def save_file(self):
        if self.file is not None:
            self.events.notify("save", self.file)
        else:
            raise FileNotFoundError("Please open a file first.")
