from LLD.Parking_Lot.Car import Car
from LLD.Parking_Lot.Level import Level
from LLD.Parking_Lot.Motorcycle import Motorcycle
from LLD.Parking_Lot.Parking_Lot import ParkingLot
from LLD.Parking_Lot.Truck import Truck
from LLD.Parking_Lot.VehicleType import VehicleType


class ParkingLotDemo:
    @staticmethod
    def run():
        parking_lot = ParkingLot.get_instance()

        # Add levels
        parking_lot.add_level(
            Level(floor=1, num_spots={VehicleType.CAR: 2, VehicleType.MOTORCYCLE: 4, VehicleType.TRUCK: 1})
        )
        parking_lot.add_level(
            Level(floor=2, num_spots={VehicleType.CAR: 4, VehicleType.MOTORCYCLE: 6, VehicleType.TRUCK: 0})
        )

        parking_lot.display_availability()

        car = Car("ABC123")
        motorcycle = Motorcycle("ABC456")
        truck = Truck("ABC789")

        # Park Vehicles
        parking_lot.park_vehicle(vehicle=car)
        parking_lot.park_vehicle(vehicle=motorcycle)
        parking_lot.park_vehicle(vehicle=truck)

        parking_lot.display_availability()

        parking_lot.unpark_vehicle(car)
        parking_lot.unpark_vehicle(motorcycle)

        parking_lot.display_availability()
