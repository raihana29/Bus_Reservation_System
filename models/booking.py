class Booking:
    def __init__(self, booking_id, passenger, bus, seats):
        self.booking_id = booking_id
        self.passenger = passenger
        self.bus = bus
        self.seats = seats
        self.status = "CONFIRMED"