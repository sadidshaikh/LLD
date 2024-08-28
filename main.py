from Design_Patterns.Behavioral_Patterns.Strategy.Context import Context
from Design_Patterns.Behavioral_Patterns.Strategy.Strategy import ConcreteStrategyA, ConcreteStrategyB

if __name__ == "__main__":
    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()
