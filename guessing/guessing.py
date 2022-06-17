import random

def play():
    print("*******************************")
    print("Welcome to the guessing game!")
    print("*******************************")

    secret_number = random.randrange(0, 101)
    total_attempt = 0
    points = 100

    print("What's your difficulty level?", secret_number)
    print("(1) - Easy")
    print("(2) - Normal")
    print("(3) - Hard")

    level = int(input("Choose your level: "))

    if(level == 1):
        total_attempt = 10
    elif(level == 2):
        total_attempt = 5
    elif(level == 3):
        total_attempt = 2

    for round in range(1, total_attempt + 1):
        print(f"Attempts {round} of {total_attempt}")

        bet_str = input("Enter your number: ")
        print("You enter number:", bet_str)
        bet = int(bet_str)

        if(bet < 1 or bet > 100):
            print("You must enter a number between 1 and 100!")
            continue

        is_right = bet == secret_number
        is_bigger = bet > secret_number
        is_smaller = bet < secret_number

        if(is_right):
            print(f"You did {points} points")
            break
        else:
            if(is_bigger):
                print("You're wrong! Your bet was bigger than the secret number.")
            elif(is_smaller):
                print("You're wrong! Your bet was smaller than the secret number.")
            lost_points = abs(secret_number - bet)
            points = points - lost_points

    print("Game Over!")

if(__name__ == "__main__"):
    play()