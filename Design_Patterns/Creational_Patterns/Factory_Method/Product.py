from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class Product1(Product):
    def operation(self) -> str:
        return "Product1 operation"


class Product2(Product):
    def operation(self) -> str:
        return "Product2 operation"
