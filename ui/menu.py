def run_menu(service):
    while True:
        print("\n1.Operator 2.Passenger 3.Exit")
        role = input("Choose: ")

        if role == "1":
            while True:
                print("\n1.Add Bus 2.Add Schedule 3.Show Buses 4.Show Schedules 5.Back")
                ch = input("Choice: ")

                if ch == "1":
                    bus_id = int(input("Bus ID: "))
                    src = input("Source: ")
                    dest = input("Destination: ")
                    seats = int(input("Seats: "))
                    price = int(input("Price: "))
                    service.add_bus(bus_id, src, dest, seats, price)

                elif ch == "2":
                    bus_id = int(input("Bus ID: "))
                    date = input("Date: ")
                    time = input("Time: ")
                    service.add_schedule(bus_id, date, time)

                elif ch == "3":
                    service.show_buses()

                elif ch == "4":
                    service.show_schedules()

                elif ch == "5":
                    break

        elif role == "2":
            while True:
                print("\n1.Search 2.Book 3.Cancel 4.Bookings 5.Back")
                ch = input("Choice: ")

                if ch == "1":
                    src = input("From: ")
                    dest = input("To: ")
                    service.search_buses(src, dest)

                elif ch == "2":
                    name = input("Name: ")
                    sid = int(input("Schedule ID: "))
                    seats = list(map(int, input("Seats (comma): ").split(",")))
                    service.book_ticket(name, sid, seats)

                elif ch == "3":
                    bid = int(input("Booking ID: "))
                    service.cancel_ticket(bid)

                elif ch == "4":
                    service.show_bookings()

                elif ch == "5":
                    break

        elif role == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")