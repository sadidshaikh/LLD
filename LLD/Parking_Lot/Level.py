from LLD.Parking_Lot.Parking_Spot import ParkingSpot
from LLD.Parking_Lot.Vehicle import Vehicle
from LLD.Parking_Lot.VehicleType import VehicleType


class Level:
    def __init__(self, floor: int, num_spots: dict[VehicleType, int]):
        self.floor = floor
        self.parking_spots: dict[VehicleType, list[ParkingSpot]] = {
            vehicle_type: [ParkingSpot(i * vehicle_type.value, vehicle_type) for i in range(spots)]
            for vehicle_type, spots in num_spots.items()
        }

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots[vehicle.get_type()]:
            if not spot.occupied and spot.get_vehicle_type() == vehicle.get_type():
                spot.park(vehicle)
                return True
        return False

    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots[vehicle.get_type()]:
            if spot.occupied and spot.get_parked_vehicle() == vehicle:
                spot.unpark()
                return True
        return False

    def display_availability(self):
        print(f"Level {self.floor} Availability:")
        for vehicle_type, spots in self.parking_spots.items():
            print(f"For {vehicle_type.name}:")
            for spot in spots:
                print(f"Spot {spot.get_spot_number()}: {'Available' if not spot.occupied else 'Occupied'}")
        print()
