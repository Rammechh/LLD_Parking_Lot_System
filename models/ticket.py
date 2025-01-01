import uuid
from datetime import datetime

class Ticket:
    def __init__(self, vehicle, parking_spot):
        self.ticket_id = str(uuid.uuid4())
        self.vehicle = vehicle
        self.parking_spot = parking_spot
        self.entry_time = datetime.now()
        self.exit_time = None
    
    def close_ticket(self):
        self.exit_time = datetime.now()
        return self.exit_time