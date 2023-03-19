"""CYOA: United Airlines Rewards Program."""
__author__ = "730412085"


from random import randint


def main() -> None:
    """Main function containing global variables."""
    points: int = 0
    player = greet()
    main_bool = False
    """Present player with at least 3 options of where to go next and ask them to choose."""
    while (main_bool == False):
        option = input(f"How can we help you today, {player}? Please enter the corresponding number from the following options: \n (1) Schedule a flight \n (2) Use my points \n (3) Exit  \n")
        if (option == '1'):
            flight(player, points)
            
        if (option == '2'):
            print(points)
        if (option == '3'):
            print(f"\nSuccessfully logged out. \n \n \n United Airlines\nGood leads the way.\U0001F6E9")
            main_bool = True



def greet() -> None:
    """Greets player and them returns to main function."""
    customer = input("Welcome to United Airlines Rewards! \n Please enter your name:  ")
    print(f"Thank you for choosing United, {customer}. \nThe United Rewards program is designed to give back to you so you can travel where you want to, anytime. \nWith each flight, you will earn points towards your next adventure. \n    Where will good lead you?")
    return (customer)
    

def flight (name: str, func_points: int) -> None:
    """Gives player choice between rates for flights."""
    flight_menu = False
    while (flight_menu == False):
        print("\U00002708  \U00002708  \U00002708  \U00002708  \U00002708  \U00002708  \U00002708  \U00002708  \U00002708  \U00002708  \U00002708  \U00002708")
        print(f"United Flights\n \nWhere will you go, {name}?")
        player_origin = input("Enter city of origin:  ")
        player_destination = input("Enter destination city:  ")
        rates_low = randint(150, 300)
        rates_high = randint(301, 600)
        rates_choice = input(f"{player_origin} to {player_destination} rates calculated from ${rates_low} to ${rates_high}. \nSelect from these rates (yes/no)?  ")
        if (rates_choice == "yes"):
            rates_func(player_origin, player_destination, rates_low, rates_high, func_points)
            return()
        else:
            return_main = input("Do you wish to return to the main menu? Enter 'yes' or 'no'.  ")
            if (return_main == 'yes'):
                return()
            else:
                print(f"Please select a new origin and destination.\n")

def rates_func(input_a: str, input_b: str, input_c: int, input_d: int, rates_points: int) -> None:
    rate_decision = False
    option_num = 1
    weekdays: list = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
    while (rate_decision == False):
        weekday_choice = weekdays[randint(0,6)]
        flight_points = randint(20, 50)
        print(f"\n------\nFlight option {option_num}: {input_a} to {input_b}\nprice: ${randint(input_c, input_d)}\n")
        flight_decision = input("Select this flight (yes/no)?  ")
        if (flight_decision == 'yes'):
            print(f"United Rewards points for Flight {option_num}: {flight_points}\nDeparts {weekday_choice}\n")
            final_decision = input(f"Confirm {flight_decision} (yes/no)?  ")
            if (final_decision == 'yes'):
                print(f"\nFlight {option_num} from {input_a} to {input_b} confirmed for {weekday_choice}\nUnited rewards points earned: {flight_points}\n \nYou may cancel anytime up until 12 hours before the start of your departure day. \nOur Help Desk is happy to assist you with any questions you may have.\n\n\U00002708  \U00002708  \U00002708")
                rates_points = rates_points + flight_points
                rate_decision = True
            else:
                return_decision = input("Do you wish to return to the flight selection menu (yes/no)?  ")
                if (return_decision == 'yes'):
                    return()
                else:
                    option_num += 1

        else:
            return_decision2 = input("Do you wish to return to the flight selection menu (yes/no)?  ")
            if (return_decision2 == 'yes'):
                return()
            else:
                option_num += 1
    return()

            


        





if __name__ == "__main__":
    main()