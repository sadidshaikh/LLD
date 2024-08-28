from Design_Patterns.Creational_Patterns.Builder.Builder import *

if __name__ == "__main__":
    builder = ConcreteBuilder1()
    builder.product_part_b()
    builder.product_part_a()
    builder.product_part_c()
    product = builder.product()
    product.list_parts()
