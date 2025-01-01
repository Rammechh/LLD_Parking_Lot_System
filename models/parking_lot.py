from .parking_floor import ParkingFloor
from .ticket import Ticket

class ParkingLot:
    def __init__(self, floors):
        self.floors = floors

    def park_vehicle(self, vehicle):
        for floor in self.floors:
            spot = floor.assign_spot(vehicle)
            if spot:
                ticket = Ticket(vehicle, spot)
                return ticket
        return None

    def remove_vehicle(self, ticket):
        ticket.parking_spot.remove_vehicle()
        ticket.close_ticket()
        return ticket
