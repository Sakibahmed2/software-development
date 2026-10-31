from user import Passenger

class Bus:
    def __init__(self, number, route, total_seat):
        self.number = number
        self.route = route
        self.total_seat = total_seat
        self.booked_seats = 0

    def available_seats(self):
        return self.total_seat - self.booked_seats

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        return False


class BusSystem:
    ticket_fare = 500

    def __init__(self):
        self.buses = []
        self.passengers = []

    def add_bus(self, number, route, seats):
        for bus in self.buses:
            if number == bus.number:
                print("A bus with this number already exist!!")
                return
        if seats <= 0:
            print("Total seats must be greater then 0")
            return
        new_bus = Bus(number, route, seats)
        self.buses.append(new_bus)
        print("Bus added successfully")

    def book_ticket(self, bus_number, name, phone):
        selected_bus = None

        for bus in self.buses:
            if bus.number == bus_number:
                selected_bus = bus
                break
        if selected_bus == None:
            print(f"Bus not found with {bus_number} this number")
            return

        if selected_bus.book_seat():
            passenger = Passenger(name, phone, selected_bus)
            self.passengers.append(passenger)

            print("\nTicket booked successfully!")
            print("------------------------------")
            print("Passenger: ", passenger.name)
            print("Phone: ", passenger.phone)
            print("Bus Number: ", selected_bus.number)
            print("Route: ", selected_bus.route)
            print("Fare: Tk", self.ticket_fare)
            print("Available Seats: ", selected_bus.available_seats())
            print("------------------------------")
        else:
            print("Sorry! No seats are available on this bus.")

    def show_buses(self):
        if len(self.buses) == 0:
            print("No bus available")
            return

        print("Available buses")
        print(f"{'Bus Number':<15}{'Route':<25}{'Total Seats':<15}{'Available Seats':<15}")
        print("-" * 75)

        for bus in self.buses:
            print(f"{bus.number:<15}{bus.route:<25}{bus.total_seat:<15}{bus.available_seats():<15}")




        

    