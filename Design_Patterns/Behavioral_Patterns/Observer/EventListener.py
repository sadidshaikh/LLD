from abc import ABC, abstractmethod


class EventListener(ABC):
    @abstractmethod
    def update(self, event_type, file):
        pass
