from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self) -> str:
        pass


class ProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of product A1"


class ProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of product A2"


class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self) -> str:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        pass


class ProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of product B1"

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of B1 collaborating with the ({result})"


class ProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of product B2"

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of B2 collaborating with the ({result})"
