class Bus:
    def __init__(self, bus_id, source, destination, total_seats, price):
        self.bus_id = bus_id
        self.source = source
        self.destination = destination
        self.total_seats = total_seats
        self.price = price
        self.available_seats = list(range(1, total_seats + 1))