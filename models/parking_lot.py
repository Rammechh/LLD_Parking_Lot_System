from .ticket import Ticket

class ParkingLot:
    def __init__(self, floors):
        self.floors = floors
    
    def park_vehicle(self, vehicle):
        for floor in self.floors:
            # Check if the floor has at least one compatible spot
            compatible = False
            for spot in floor.spots:
                if spot.vehicle_type == vehicle.get_vehicle_type():
                    compatible = True
                    break  # No need to check further spots
            if compatible:
                spot = floor.assign_spot(vehicle)
                if spot:
                    ticket = Ticket(vehicle, spot)
                    return ticket
        return None
    
    def remove_vehicle(self, ticket):
        ticket.parking_spot.remove_vehicle()
        ticket.close_ticket()
        return ticket
