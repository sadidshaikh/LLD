# Wrong

class Vehicle:
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print('Starting engine')


class Bicycle(Vehicle):
    def start_engine(self):
        # Does not make sense
        pass


# Correct

class Vehicle:
    def start(self):
        raise NotImplementedError


class Car(Vehicle):
    def start(self):
        print("starting the car engine")


class Bicycle(Vehicle):
    def start(self):
        print("Pedaling the bibycle...")
