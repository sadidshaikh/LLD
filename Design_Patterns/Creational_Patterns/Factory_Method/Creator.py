from abc import ABC, abstractmethod
from Design_Patterns.Creational_Patterns.Factory_Method.Product import Product, Product1, Product2


class Creator(ABC):
    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Some operation on {product.operation()}"

    @abstractmethod
    def factory_method(self) -> Product:
        pass


class CreatorProduct1(Creator):
    def factory_method(self) -> Product:
        return Product1()


class CreatorProduct2(Creator):
    def factory_method(self) -> Product:
        return Product2()
