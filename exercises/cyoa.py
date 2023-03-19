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
            rewards(points, player)
        if (option == '3'):
            print(f"\nSuccessfully logged out. \n \n \n United Airlines\nGood leads the way.\U0001F6E9")
            main_bool = True



def greet() -> None:
    """Greets player and them returns to main function."""
    customer = input("Welcome to United Airlines Rewards! \n Please enter your name:  ")
    print(f"Thank you for choosing United, {customer}. \nThe United Rewards program is designed to give back to you so you can travel where you want to, anytime. \nWith each flight, you will earn points towards your next adventure. \n    Where will good lead you? \U0001F6E9")
    return (customer)
    

def flight (name: str, func_points: int) -> None:
    """Gives player choice between rates for flights."""
    flight_menu = False
    while (flight_menu == False):
        print("\U00002708  \U00002708  \U00002708  \U00002708  \U00002708  \U00002708  \U00002708  \U00002708  \U00002708  \U00002708  \U00002708  \U00002708")
        print(f"United Flights \n \nWhere will you go, {name}?")
        player_origin = input("Enter city of origin:  ")
        player_destination = input("Enter destination city:  ")
        rates_low = randint(150, 300)
        rates_high = randint(301, 600)
        rates_choice = input(f"{player_origin} to {player_destination} rates calculated from ${rates_low} to ${rates_high}. \nSelect from these rates? Enter 'yes' or 'no'.  ")
        if (rates_choice == "yes"):
            rates_func(player_origin, player_destination, rates_low, rates_high, func_points)
            flight_menu = True
        else:
            return_main = input("Do you wish to return to the main menu or the flight selection menu? Enter 'main menu' or 'flight menu'.  ")
            if (return_main == 'main menu'):
                return()
            else:
                print(f"Please select a new origin and destination.\n")
    return()

def rates_func(input_a: str, input_b: str, input_c: int, input_d: int, rates_points: int) -> None:
    rate_decision = False
    option_num = 1
    weekdays: list = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
    while (rate_decision == False):
        weekday_choice = weekdays[randint(0,6)]
        flight_points = randint(20, 50)
        print(f"\n------\nFlight option {option_num}: {input_a} to {input_b}\nprice: ${randint(input_c, input_d)}\n")
        flight_decision = input("Select this flight? Enter 'yes' or 'no'  ")
        if (flight_decision == 'yes'):
            print(f"United Rewards points for Flight {option_num}: {flight_points}\nDeparts {weekday_choice}\n")
            final_decision = input(f"Confirm {flight_decision}? Enter 'yes' or 'no'.  ")
            if (final_decision == 'yes'):
                print(f"\nFlight {option_num} from {input_a} to {input_b} confirmed for {weekday_choice}\nUnited rewards points earned: {flight_points}\n \nYou may cancel with no penalty anytime up until 12 hours before the start of your departure day. \nAll Rewards points earned will be added to your account within 4 hours. \nOur Help Desk is happy to assist you with any questions you may have.\n\n\U0001F6EB  \U0001F6EB  \U0001F6EB")
                rates_points = rates_points + flight_points
                rate_decision = True
            else:
                return_decision = input("Do you wish to return to the main menu or to view an alternate flight for your trip? Enter 'main menu' or 'view new flight'.  ")
                if (return_decision == 'main menu'):
                    rate_decision = True
                else:
                    option_num += 1

        else:
            return_decision2 = input("Do you wish to return to the main menu or to view an alternate flight for your trip? Enter 'main menu' or 'view new flight'.  ")
            if (return_decision2 == 'main menu'):
                return()
            else:
                option_num += 1
    return()

            
def rewards(rewards_points: int, rewards_name: str) -> int:
    rewards_points = rewards_points + randint(0,120)
    print(f"Thank you for flying with us, {rewards_name}!\nYour current total Rewards points are {rewards_points}")
    rewards_choice = input("Would you like to use your points or return to the main menu? Enter 'use points' or 'main menu'.  ")
    if (rewards_choice == 'use points'):
        points_use = input(f"Please select from the following options: \n (1) Use points to upgrade seat on current flight.\n(2) Use points to discount future flight.\n(3) Use points to purchase wifi for current flight. \n")
        if (rewards_points == 0):
            print(f"\nYou currently don't have any points with us. \n---\nRedirecting you to the main menu.")
            return()
        if (points_use == '1'):
            print("ok dork")
    else:
        print("no")




if __name__ == "__main__":
    main()