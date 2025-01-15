from colorama import Fore, Style

class Flight:
    flight_count = 0

    def __init__(self, flight_number, from_, to, seats):
        self.flight_number = flight_number
        self.from_ = from_
        self.to = to
        self.seats = seats
        self.booked_seats = 0
        Flight.flight_count += 1

    def __str__(self):
        return f"Flight {self.flight_number}: {self.from_} to {self.to}"

    def check_availability(self):
        return self.seats - self.booked_seats

    def book_seat(self):
        if self.check_availability() > 0:
            self.booked_seats += 1
            return f"Seat booked on {self.flight_number}."
        else:
            return "No seats available."


class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number

    def __str__(self):
        return f"Passenger {self.name}, Passport: {self.passport_number}"


class AirlineManager:
    def __init__(self):
        self.flights = []
        self.passengers = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def add_passengers(self, passenger):
        self.passengers.append(passenger)

    def get_flights(self):
        print(Fore.CYAN + "List of flights:" + Style.RESET_ALL)
        for flight in self.flights:
            print(flight)

    def get_passengers(self):
        print(Fore.YELLOW + "List of passengers:" + Style.RESET_ALL)
        for passenger in self.passengers:
            print(passenger)

    def validate_pasport(passport_number):
        return len(passport_number) == 9 and passport_number.isdigit()



def booking_luggages(func):
    def wrapper(*args):
        result = func(*args)
        print(Fore.LIGHTGREEN_EX + f"Process complited: " + Style.RESET_ALL, result)
        return result
    return wrapper


@booking_luggages
def book_seat(flight, passenger):
    if  AirlineManager.validate_pasport(passenger.passport_number):
        return flight.book_seat()
    else:
        return Fore.RED + "Invalid passport number." + Style.RESET_ALL



manager = AirlineManager()

flight1 = Flight("UZ123", "Tashkent", "London", 150)
flight2 = Flight("UZ456", "Tashkent", "New York", 200)
manager.add_flight(flight1)
manager.add_flight(flight2)

passenger1 = Passenger("Ali", "123456789")
passenger2 = Passenger("Vali", "987654321")
passenger3 = Passenger("Karim", "121212321")
passenger4 = Passenger("Botir", "334343434341")
manager.add_passengers(passenger1)
manager.add_passengers(passenger2)
manager.add_passengers(passenger3)
manager.add_passengers(passenger4)



# print(flight1.booked_seats)

book_seat(flight1, passenger1)
book_seat(flight2, passenger2)

manager.get_flights()
manager.get_passengers()
