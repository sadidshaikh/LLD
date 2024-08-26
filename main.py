from Design_Patterns.Creational_Patterns.Factory_Method.Creator import Creator, CreatorProduct1, CreatorProduct2


def client_code(creator: Creator):
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(CreatorProduct1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(CreatorProduct2())
