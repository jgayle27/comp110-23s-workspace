"""CYOA: United Airlines Rewards Program."""
__author__ = "730412085"


from random import randint

player: str
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
            points = rewards(points, player)
            print(points)
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
                return ()
            else:
                print(f"Please select a new origin and destination.\n")
    return ()


def rates_func(input_a: str, input_b: str, input_c: int, input_d: int, rates_points: int) -> None:
    """Inputs destination and origin and rate bounds to give player the opportunity to choose a rate and flight number to book a flight."""
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
                return ()
            else:
                option_num += 1
    return ()

            
def rewards(rewards_points: int, rewards_name: str) -> int:
    """Inputs points and player name to give player the opportunity to choose what they want to do with their points."""
    rewards_points += randint(0,120)
    print(f"Thank you for flying with us, {rewards_name}!\nYour current Rewards points total is {rewards_points}")
    rewards_choice = input("Would you like to use your points or return to the main menu? Enter 'use points' or 'main menu'.  ")
    if (rewards_choice == 'use points'):
        if (rewards_points == 0):
            print(f"\nYou currently don't have any points with us. \n---\nRedirecting you to the main menu.\n")
            return(rewards_points)
        points_use = input(f"Please select from the following options: \n(1) Use points to upgrade seat on current flight.\n(2) Use points to discount future flight.\n(3) Use points to purchase wifi for current flight. \n")
        if (points_use == '1'):
            rewards_points = seat_upgrade(rewards_points)
        if (points_use == '2'):
            rewards_points = discount_flight(rewards_points)
        if (points_use == '3'):
            rewards_points = wifi(rewards_points)
    else:
        return(rewards_points)

def seat_upgrade(seat_points: int) -> int:
    """Inputs points and flight number to determine seat upgrade cost and outputs new point amount."""
    flight_num = input(f"-----\nWhat is your flight number?  ")
    if (flight_num <= '500'):
        seat_amount = randint(0,30)
        print(f"Points required to update your seat on flight {flight_num} is {seat_amount}.")
        upgrade_choice = input("Use your points to upgrade seat? Enter 'yes' or 'no'.  ")
        if (upgrade_choice == 'yes'):
            if (seat_points < seat_amount):
                print(f"Your current rewards balance is unable to cover this upgrade. Redirecting you to the points selection menu.\n")
                return (seat_points)
            seat_points = seat_points - seat_amount
            print(f"Your seat has been upgraded. Your remaining Rewards points balance is {seat_points}")
            return (seat_points)
        else:
            return (seat_points)
    else:
        seat_amount = randint(31,60)
        print(f"Points required to update your seat on flight {flight_num} is {seat_amount}.")
        upgrade_choice = input("Use your points to upgrade seat? Enter 'yes' or 'no'.  ")
        if (upgrade_choice == 'yes'):
            if (seat_points < seat_amount):
                print(f"Your current rewards balance is unable to cover this upgrade. Redirecting you to the points selection menu.\n")
                return (seat_points)
            seat_points = seat_points - seat_amount
            print(f"Your seat has been upgraded. Your remaining Rewards points balance is {seat_points}")
            return (seat_points)
        else:
            return (seat_points)


def discount_flight(discount_points: int) -> int:
    """Uses flight number and points to discount flight price and output a new point amount."""
    flight_num = input(f"-----\nWhat is your flight number? Enter number from '100' to '1000'  ")
    if (flight_num <= '800'):
        flight_discount = randint(0,30)
        flight_cost = randint(150,300)
        if (discount_points - flight_discount <= 0):
            print(f"Your flight is not eligible for discount. \n----\nRedirecting you to the main menu.")
            return (discount_points)
        if (flight_cost - flight_discount*1.7 <= 0):
            print(f"Your flight is not eligible for discount. \n----\nRedirecting you to the main menu.")
            return (discount_points)
        else:
            new_flight_cost = flight_cost - flight_discount*1.7
        if (new_flight_cost >= 80):
            print(f"Your discounted flight total is calculated to be:  ${new_flight_cost} from original cost of ${flight_cost}.")
            discount_choice = input("Use your points to discount your flight? Enter 'yes' or 'no'.  ")
            if (discount_choice == 'yes'):
                discount_points = discount_points - flight_discount
                print(f"Your flight has been discounted. Your remaining Rewards points balance is {discount_points}")
                return (discount_points)
        else:
            discount_points = discount_points - flight_discount
            print(f"Your flight is eligible for a bonus discount bringing your flight's total to $0. Your remaining Rewards points balance is {discount_points}\nThank you for being a frequent flyer!")
            flight_cost = 0
            return (discount_points)
    else:
        flight_discount = randint(31,60)
        flight_cost = randint(301,600)
        if (discount_points - flight_discount <= 0):
            print(f"Your flight is not eligible for discount. \n----\nRedirecting you to the main menu.")
            return (discount_points)
        if (flight_cost - flight_discount*1.7 <= 0):
            print(f"Your flight is not eligible for discount. \n----\nRedirecting you to the main menu.")
            return (discount_points)
        else:
            new_flight_cost = flight_cost - flight_discount*1.7
        if (new_flight_cost >= 100):
            print(f"Your discounted flight total is calculated to be:  ${new_flight_cost} from original cost of ${flight_cost}.")
            discount_choice = input("Use your points to discount your flight? Enter 'yes' or 'no'.  ")
            if (discount_choice == 'yes'):
                discount_points = discount_points - flight_discount
                print(f"Your flight has been discounted. Your remaining Rewards points balance is {discount_points}")
                return (discount_points)
        else:
            discount_points = discount_points - flight_discount
            print(f"Your flight is eligible for a bonus discount bringing your flight's total to $0. Your remaining Rewards points balance is {discount_points}\nThank you for being a frequent flyer!")
            flight_cost = 0
            return (discount_points)
    return (discount_points)


def wifi(wifi_points: int) -> int:
    """Takes points and sees if player can purchase wifi. If player purchases wifi, adjusts points accordingly."""
    print("United Airlines is proud to provide guest wifi on all of its flights. \nHowever, for $10 dollars or 8 points, you may purchase specialty wifi which allows for internet surfing, texting, and emailing while flying.\nOur Rewards program allows for members to use points to purchase this wifi. ")
    use_wifi = input(f"\nWould you like to use your points towards our specialty wifi or return to the main menu? Enter 'use points' or 'main menu'.  ")
    if (use_wifi == 'use points'):
        if (wifi_points == 0):
            print(f"Your current Rewards points balance is 0. Unfortunately you cannot purchase wifi at this time.\n----\nRedirecting you to the main menu.\n")
            return (wifi_points)
        else:
            if (wifi_points < 8):
                print(f"Your current Rewards points balance is {wifi_points}. Unfortunately you cannot purchase wifi at this time.\n----\nRedirecting you to the main menu.\n")
                return (wifi_points)
            else:
                wifi_points = wifi_points - 8
                print(f"Your current Rewards points balance is {wifi_points}. Thank you for choosing United. We look forward to seeing you\U00002708\n----\nRedirecting you to the main menu.\n")
                return (wifi_points)
    else:        
        return (wifi_points)




if __name__ == "__main__":
    main()