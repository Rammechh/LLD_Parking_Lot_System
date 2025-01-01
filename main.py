from models.parking_floor import ParkingFloor
from models.parking_lot import ParkingLot
from models.vehicle import Vehicle
from models.payment import Payment

# Setup Parking Lot
floor1 = ParkingFloor(1, 5)
floor2 = ParkingFloor(2, 5)
parking_lot = ParkingLot([floor1, floor2])

# Park a Vehicle
car = Vehicle('car', 'ABC123')
ticket = parking_lot.park_vehicle(car)
if ticket:
    print(f"Vehicle parked. Ticket ID: {ticket.ticket_id}, Spot: {ticket.parking_spot.spot_id}")
else:
    print("No available spots.")

# Remove Vehicle
if ticket:
    parking_lot.remove_vehicle(ticket)
    payment = Payment(ticket)
    print(f"Parking fee: ${payment.calculate_fee():.2f}")
