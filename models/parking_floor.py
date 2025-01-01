from .parking_spot import ParkingSpot
class ParkingFloor:
    def __init__(self, floor_id, floor_capacity, vehicle_type="car"):
        self.floor_id = floor_id
        self.spots = [
            ParkingSpot(f"{floor_id}-{i}", vehicle_type) for i in range(floor_capacity)
        ]
    
    def get_available_spots(self):
        return [spot for spot in self.spots if spot.is_available]
    
    def assign_spot(self, vehicle):
        for spot in self.get_available_spots():
            if spot.assign_vehicle(vehicle):
                return spot
        return None