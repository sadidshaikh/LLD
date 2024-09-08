from LLD.Parking_Lot.Level import Level
from LLD.Parking_Lot.Vehicle import Vehicle


class ParkingLot:
    _instance = None

    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("This class is singleton!")
        else:
            ParkingLot._instance = self
            self.levels: list[Level] = []

    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot._instance = ParkingLot()
        return ParkingLot._instance

    def add_level(self, level: Level):
        self.levels.append(level)

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False

    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True
        return False

    def display_availability(self):
        for level in self.levels:
            level.display_availability()
