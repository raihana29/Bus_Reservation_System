# Bus Reservation System

## Problem Statement
Design and implement a Bus Reservation System for an inter-city bus operator.

The system should allow:

### Passengers
- Search buses based on source and destination
- View available seats
- Book tickets by selecting seats
- Cancel bookings with applicable charges

### Operators
- Manage fleet (add buses)
- Create and manage schedules (date & time)

---

## Approach / Logic Used
The system is designed using Object-Oriented Programming (OOP) principles.

### Core Components
- **Bus** → Stores route details and seat availability
- **Schedule** → Represents a trip for a bus with date & time
- **Passenger** → Stores passenger details
- **Booking** → Stores booking details and status
- **BusSystem** → Controls the entire system

---

## Key Logic
- Search buses using source & destination
- Seat allocation using list of seats
- Booking checks seat availability and assigns booking ID
- Cancellation restores seats and applies 10% charge

---

## Steps to Execute the Code

### 1. Save the file
bus_reservation.py

### 2. Run the program
python main.py

### 3. Use the menu

#### Operator Flow
1. Add Bus
2. Add Schedule

#### Passenger Flow
1. Search buses
2. Book seats
3. Cancel booking

---

## Technologies Used
- Python
- Object-Oriented Programming
