from .parking_spot import ParkingSpot
class ParkingFloor:
    def __init__(self, floor_id, floor_capacity, vehicle_type="car"):
        self.floor_id = floor_id
        self.spots = []
        for i in range(floor_capacity):
            spot_id = f"{floor_id}-{i}"
            spot = ParkingSpot(spot_id, vehicle_type)
            self.spots.append(spot)
    
    def get_available_spot(self):
        return [spot for spot in self.spots if spot.is_available]
    
    def assign_spot(self, vehicle):
        for spot in self.get_available_spot():
            if spot.is_available and spot.vehicle_type == vehicle.get_vehicle_type():
                if spot.assign_vehicle(vehicle):
                    return spot
        return None