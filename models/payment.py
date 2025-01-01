from datetime import datetime

class Payment:
    def __init__(self, ticket, rate_per_hour = 10):
        self.ticket = ticket
        self.rate_per_hour = rate_per_hour
        self.amount_due = 0
    
    def calculate_fee(self):
        entry_time = self.ticket.entry_time
        exit_time = self.ticket.exit_time or datetime.now()
        duration = (exit_time - entry_time).total_seconds() / 3600
        self.amount_due = max(1, round(duration)) * self.rate_per_hour
        return self.amount_due