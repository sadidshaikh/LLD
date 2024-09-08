from abc import ABC, abstractmethod

from LLD.Parking_Lot.VehicleType import VehicleType


class Vehicle(ABC):
    def __init__(self, licence_plate: str, vehicle_type: VehicleType):
        self.licence_plate = licence_plate
        self.type = vehicle_type

    def get_type(self) -> VehicleType:
        return self.type
