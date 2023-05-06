
class PlaneTicket:

    departure_city: str
    arrival_city: str
    departure_time: int
    ticket_cost: float

    def __init__(self, city_a: str, city_b: str, depart: int, cost: float):
        """Initialize ticket object."""
        self.departure_city = city_a
        self.arrival_city = city_b
        self.departure_time = depart
        self.ticket_cost = cost

    def __str__(self) -> str:
        """Make it prettier."""
        ticket_str: str = f"Flight from {self.departure_city} at {self.departure_time}. "
        ticket_str += f"Arrive in {self.arrival_city}. Costs {self.ticket_cost}."
        return ticket_str
    
    def delay(self, delay_hours: int) -> None:
        """Update departure time."""
        self.departure_time = self.departure_time + (delay_hours * 100)

    # def __mul__(self, a: float, b: float) -> float:
    #      """Mutiply variables"""
    #      return a * b

    def discount(self, discount: float) -> None:
        """Update ticket cost."""
        self.ticket_cost = self.ticket_cost - (self.ticket_cost * discount)


    

# Function so move out of class
def compare_prices(ticket1: PlaneTicket, ticket2: PlaneTicket) -> PlaneTicket:
        """Compare ticket prices."""
        if ticket1.ticket_cost < ticket2.ticket_cost:
             return ticket1
        else: #ticket1 >= ticket2
             return ticket2
        


ticket: PlaneTicket = PlaneTicket("a", "b", 1200, 10.50)
# ticket.delay(2)
# print(ticket)

my_ticket: PlaneTicket = PlaneTicket("Raleigh", "New Orleans", 1000, 85.25)
# print(my_ticket)
my_ticket.delay(2)
my_ticket.discount(.10)
ur_ticket: PlaneTicket = PlaneTicket("Orlando", "San Fransisco", 1100, 100.50)
print(compare_prices(my_ticket, ur_ticket))