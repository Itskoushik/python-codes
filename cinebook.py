'''
Title: Cinebook - movie ticket booking sys
core features that i will try to cover.
browse movies and showtimes, select seats 
book tickets view booking history 

addons: add food snacks , payment or admin portal

'''

import random

# Movie class
class Movie:
    def __init__(self, movie_id, name, genre, duration):
        self.movie_id = movie_id
        self.name = name
        self.genre = genre
        self.duration = duration

    def display_info(self):
        print(f"[{self.movie_id}] {self.name} | Genre: {self.genre} | Duration: {self.duration} mins")

# Seat class
class Seat:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.is_booked = False

    def book(self):
        if not self.is_booked:
            self.is_booked = True
            return True
        return False

    def __str__(self):
        return "X" if self.is_booked else "O"

# Showtime class
class Showtime:
    def __init__(self, time, movie):
        self.time = time
        self.movie = movie
        self.seats = [[Seat(r, c) for c in range(5)] for r in range(5)]  # 5x5 layout seating created for the user

    def display(self, index):
        print(f"{index}. {self.movie.name} at {self.time}")

    def show_seats(self):
        print("\nSeat Layout (O=Available, X=Booked):")
        for row in self.seats:
            print(" ".join(str(seat) for seat in row))
        print("Enter row and column (0-based) to book (e.g., 0 1)")

    def book_seats(self, seat_coords):
        booked = []
        for r, c in seat_coords:
            if 0 <= r < 5 and 0 <= c < 5 and self.seats[r][c].book():
                booked.append((r, c))
            else:
                print(f"Seat ({r},{c}) is already booked or invalid.")
        return booked

# Screen class
class Screen:
    def __init__(self, screen_id, showtimes):
        self.screen_id = screen_id
        self.showtimes = showtimes

    def display_showtimes(self):
        print(f"\nScreen {self.screen_id}:")
        for i, show in enumerate(self.showtimes):
            show.display(i)

# Theatre class
class Theatre:
    def __init__(self, name, screens):
        self.name = name
        self.screens = screens

    def display_theatre(self):
        print(f"\nWelcome to {self.name}!")
        for screen in self.screens:
            screen.display_showtimes()

    def get_all_showtimes(self):
        showtimes = []
        for screen in self.screens:
            showtimes.extend(screen.showtimes)
        return showtimes

# Booking class
class Booking:
    def __init__(self, user, showtime, seats):
        self.user = user
        self.showtime = showtime
        self.seats = seats
        self.booking_id = random.randint(1000, 9999)

    def display_booking(self):
        print(f"\n Booking ID: {self.booking_id}")
        print(f"Movie: {self.showtime.movie.name}")
        print(f"Time: {self.showtime.time}")
        print(f"Seats: {', '.join([f'({r},{c})' for r, c in self.seats])}")

# User class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.bookings = []

    def book_ticket(self, showtime):
        showtime.show_seats()
        n = int(input("How many seats do you want to book? "))
        seat_coords = []
        for _ in range(n):
            r, c = map(int, input("Enter row and column: ").split())
            seat_coords.append((r, c))

        booked = showtime.book_seats(seat_coords)
        if booked:
            booking = Booking(self, showtime, booked)
            self.bookings.append(booking)
            print("\n Booking successful!")
            booking.display_booking()
        else:
            print(" Booking failed. Try again.")

    def view_bookings(self):
        if not self.bookings:
            print("\nYou have no bookings yet.")
        else:
            print(f"\n🧾 {self.name}'s Bookings:")
            for booking in self.bookings:
                booking.display_booking()

# Sample Data
movies=[ Movie(1,"F1: The Movie","Action,Drama,Sports",155)
        ,Movie(2,"Kantara: A Legend Chapter-1","Adventure,Drama,Thriller",180)
        ,Movie(3,"Saiyarra","Drama,Musical,Romantic",156)
        ,Movie(4,"Su From So","Comedy,Horror",130)
        ,Movie(5,"Conjuring: last rites","Horror",180)
        ,Movie(6,"Dhadak 2","Drama,Romantic",146)
        ]

showtimes_screen1 = [
    Showtime("10:00 AM", movies[0]),
    Showtime("3:00 PM", movies[1]),
]

showtimes_screen2 = [
    Showtime("4:00 PM", movies[4]),
    Showtime("7:00 PM", movies[0]),
]

showtimes_screen3 = [
    Showtime("09:00 AM", movies[1]),
    Showtime("1:00 PM", movies[3]),
]

showtimes_screen4 = [
    Showtime("4:00 PM", movies[2]),
    Showtime("9:00 PM", movies[3]),
]

showtimes_screen5 = [
    Showtime("2:00 PM", movies[2]),
    Showtime("5:00 PM", movies[4]),
]

screens = [
    Screen(1, showtimes_screen1),
    Screen(2, showtimes_screen2),
    Screen(3, showtimes_screen3),
    Screen(4, showtimes_screen4),
    Screen(5, showtimes_screen5),
]

theatre = Theatre("CineBook Cinemas", screens)

# Main Program
def main():
    print("🎬 Welcome to CineBook Terminal App 🎬")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    user = User(name, email)

    while True:
        print("\nMain Menu:")
        print("1. View Showtimes")
        print("2. Book Ticket")
        print("3. View My Bookings")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            theatre.display_theatre()

        elif choice == '2':
            all_showtimes = theatre.get_all_showtimes()
            print("\nSelect a show to book:")
            for i, show in enumerate(all_showtimes):
                show.display(i)
            idx = int(input("Enter show index: "))
            if 0 <= idx < len(all_showtimes):
                user.book_ticket(all_showtimes[idx])
            else:
                print("Invalid selection.")

        elif choice == '3':
            user.view_bookings()

        elif choice == '4':
            print("Thanks for using CineBook. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
