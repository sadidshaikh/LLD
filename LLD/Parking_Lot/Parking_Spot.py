from LLD.Parking_Lot.Vehicle import Vehicle
from LLD.Parking_Lot.VehicleType import VehicleType


class ParkingSpot:
    def __init__(self, spot_number: int, vehicle_type: VehicleType = VehicleType.CAR):
        self.spot_number = spot_number
        self.vehicle_type = vehicle_type
        self.occupied = False
        self.parked_vehicle = None

    def park(self, vehicle: Vehicle):
        if self.occupied or vehicle.get_type() != self.vehicle_type:
            raise ValueError("Invalid vehicle type or spot already occupied")
        self.occupied = True
        self.parked_vehicle = vehicle

    def unpark(self):
        self.occupied = False
        self.parked_vehicle = None

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_spot_number(self):
        return self.spot_number

    def get_parked_vehicle(self):
        return self.parked_vehicle
