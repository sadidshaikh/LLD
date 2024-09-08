from LLD.Parking_Lot.Vehicle import Vehicle
from LLD.Parking_Lot.VehicleType import VehicleType


class Car(Vehicle):
    def __init__(self, licence_plate: str):
        super().__init__(licence_plate, VehicleType.CAR)
