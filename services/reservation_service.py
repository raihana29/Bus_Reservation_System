from models.passenger import Passenger
from models.operator import Operator
from models.bus import Bus
from models.schedule import Schedule
from models.booking import Booking


class BusReservationService:
    def __init__(self):
        self.buses = []
        self.schedules = []
        self.bookings = {}

        self.booking_id = 1
        self.passenger_id = 1
        self.schedule_id = 1

    def add_bus(self, bus_id, source, destination, seats, price):
        bus = Bus(bus_id, source, destination, seats, price)
        self.buses.append(bus)
        print("Bus added successfully")

    def add_schedule(self, bus_id, date, time):
        bus = next((b for b in self.buses if b.bus_id == bus_id), None)

        if not bus:
            print("Bus not found")
            return

        schedule = Schedule(self.schedule_id, bus, date, time)
        self.schedules.append(schedule)
        self.schedule_id += 1

        print("Schedule added successfully")

    def show_buses(self):
        print("\n--- Buses ---")
        if not self.buses:
            print("No buses available")
            return

        for b in self.buses:
            print(f"Bus {b.bus_id} | {b.source}->{b.destination} | Price:{b.price}")

    def show_schedules(self):
        print("\n--- Schedules ---")
        if not self.schedules:
            print("No schedules available")
            return

        for s in self.schedules:
            print(f"Schedule {s.schedule_id} | Bus {s.bus.bus_id} | {s.date} {s.time}")

    def search_buses(self, source, destination):
        result = []

        for s in self.schedules:
            if s.bus.source == source and s.bus.destination == destination:
                result.append(s)

        if not result:
            print("No buses found")
            return []

        print("\nAvailable Buses:")
        for s in result:
            b = s.bus
            print(f"Schedule {s.schedule_id} | Bus {b.bus_id} | {b.source}->{b.destination} | Seats:{len(b.available_seats)} | Time:{s.time}")

        return result

    def book_ticket(self, name, schedule_id, seats):
        schedule = next((s for s in self.schedules if s.schedule_id == schedule_id), None)

        if not schedule:
            print("Invalid schedule ID")
            return

        bus = schedule.bus

        for seat in seats:
            if seat not in bus.available_seats:
                print(f"Seat {seat} not available")
                return

        passenger = Passenger(self.passenger_id, name)
        self.passenger_id += 1

        for seat in seats:
            bus.available_seats.remove(seat)

        booking = Booking(self.booking_id, passenger, bus, seats)
        self.bookings[self.booking_id] = booking
        self.booking_id += 1

        print(f"Booking successful! ID: {booking.booking_id}")

    def cancel_ticket(self, booking_id):
        booking = self.bookings.get(booking_id)

        if not booking or booking.status == "CANCELLED":
            print("Invalid booking")
            return

        refund = len(booking.seats) * booking.bus.price * 0.9

        for seat in booking.seats:
            booking.bus.available_seats.append(seat)

        booking.status = "CANCELLED"
        print(f"Cancelled. Refund: {refund}")

    def show_bookings(self):
        print("\n--- Bookings ---")
        if not self.bookings:
            print("No bookings found")
            return

        for b in self.bookings.values():
            print(f"{b.booking_id} | {b.passenger.name} | Bus {b.bus.bus_id} | Seats {b.seats} | {b.status}")