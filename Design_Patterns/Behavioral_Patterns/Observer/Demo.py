from Design_Patterns.Behavioral_Patterns.Observer.Editor import Editor
from Design_Patterns.Behavioral_Patterns.Observer.EmailNotificationListener import EmailNotificationListener
from Design_Patterns.Behavioral_Patterns.Observer.LogOpenListener import LogOpenListener


class Demo:
    @staticmethod
    def run():
        editor = Editor()

        editor.events.subscribe("open", EmailNotificationListener("sadid@gmail.com"))
        editor.events.subscribe("open", LogOpenListener("/path/to/log/file.txt"))
        editor.events.subscribe("save", EmailNotificationListener("admin@gmail.com"))

        editor.open_file("test_file.txt")
        editor.save_file()
