class ParkingSpot:
    def __init__(self, spot_id, vehicle_type):
        self.spot_id = spot_id
        self.vehicle_type = vehicle_type
        self.is_available = True
        self.vehicle = None
    
    def assign_vehicle(self, vehicle):
        if self.is_available and vehicle.get_vehicle_type() == self.vehicle_type:
            self.vehicle = vehicle
            self.is_available = False
            return True
        return False

    def remove_vehicle(self):
        self.vehicle = None
        self.is_available = True 