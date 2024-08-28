from abc import ABC, abstractmethod

from Design_Patterns.Creational_Patterns.Builder.Product import Product1


class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def product_part_a(self) -> None:
        pass

    @abstractmethod
    def product_part_b(self) -> None:
        pass

    @abstractmethod
    def product_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def product_part_a(self) -> None:
        self._product.add("PartA1")

    def product_part_b(self) -> None:
        self._product.add("PartB1")

    def product_part_c(self) -> None:
        self._product.add("PartC1")
