from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: list):
        pass


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: list) -> list:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: list) -> list:
        return list(reversed(sorted(data)))
