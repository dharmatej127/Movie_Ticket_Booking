# OOP Implementation

class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration  # in minutes

class Theater:
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.available_seats = set(range(1, total_seats + 1))  # Seat numbers

class Ticket:
    def __init__(self, movie, theater, seat_number, price=200):
        self.movie = movie
        self.theater = theater
        self.seat_number = seat_number
        self.price = price

class BookingSystem:
    def __init__(self):
        self.bookings = []  # store all tickets

    def book_ticket(self, movie, theater, seat_number):
        if seat_number not in theater.available_seats:
            raise ValueError(f"Seat {seat_number} is already booked.")
        theater.available_seats.remove(seat_number)
        ticket = Ticket(movie, theater, seat_number)
        self.bookings.append(ticket)
        return ticket

    def cancel_ticket(self, ticket):
        if ticket in self.bookings:
            self.bookings.remove(ticket)
            ticket.theater.available_seats.add(ticket.seat_number)
            return f"Refund of ₹{ticket.price} processed."
        else:
            raise ValueError("Ticket not found in bookings.")





# --- Driver Code to See Output ---
movie = Movie("Inception", 148)
theater = Theater("PVR Cinemas", 5)
system = BookingSystem()

# Booking tickets
print("---- Booking Tickets ----")
ticket1 = system.book_ticket(movie, theater, 1)
print(f"Booked Seat {ticket1.seat_number} for {ticket1.movie.title} in {ticket1.theater.name}")

ticket2 = system.book_ticket(movie, theater, 2)
print(f"Booked Seat {ticket2.seat_number} for {ticket2.movie.title} in {ticket2.theater.name}")

# Trying to book the same seat again (should raise error)
print("\n---- Double Booking Test ----")
try:
    system.book_ticket(movie, theater, 2)
except ValueError as e:
    print("Error:", e)

# Cancelling a ticket
print("\n---- Cancellation ----")
refund_msg = system.cancel_ticket(ticket1)
print(refund_msg)

# Checking available seats after cancellation
print("Available Seats:", theater.available_seats)




import unittest

class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Theater:
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.available_seats = set(range(1, total_seats + 1))

class Ticket:
    def __init__(self, movie, theater, seat_number, price=200):
        self.movie = movie
        self.theater = theater
        self.seat_number = seat_number
        self.price = price

class BookingSystem:
    def __init__(self):
        self.bookings = []

    def book_ticket(self, movie, theater, seat_number):
        if seat_number not in theater.available_seats:
            raise ValueError(f"Seat {seat_number} is already booked.")
        theater.available_seats.remove(seat_number)
        ticket = Ticket(movie, theater, seat_number)
        self.bookings.append(ticket)
        return ticket

    def cancel_ticket(self, ticket):
        if ticket in self.bookings:
            self.bookings.remove(ticket)
            ticket.theater.available_seats.add(ticket.seat_number)
            return f"Refund of ₹{ticket.price} processed."
        else:
            raise ValueError("Ticket not found in bookings.")

class TestBookingSystem(unittest.TestCase):
    def setUp(self):
        self.movie = Movie("Inception", 148)
        self.theater = Theater("PVR", 5)
        self.system = BookingSystem()

    def test_seat_availability_after_booking(self):
        ticket = self.system.book_ticket(self.movie, self.theater, 1)
        self.assertNotIn(1, self.theater.available_seats)

    def test_double_booking_not_allowed(self):
        self.system.book_ticket(self.movie, self.theater, 2)
        with self.assertRaises(ValueError):
            self.system.book_ticket(self.movie, self.theater, 2)

    def test_cancellation_restores_seat_and_refund(self):
        ticket = self.system.book_ticket(self.movie, self.theater, 3)
        refund_msg = self.system.cancel_ticket(ticket)
        self.assertIn(3, self.theater.available_seats)
        self.assertEqual(refund_msg, "Refund of ₹200 processed.")

# Run tests (works both in script & Jupyter)
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)


