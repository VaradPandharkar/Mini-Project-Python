import random 

lowest_num = 1
highest_num = 100
answers = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number Between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your Guess: ")
    if  guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please Select a number Between {lowest_num} and {highest_num}")

        elif guess < answers:
            print("To Low! try again!")
        elif guess > answers:
            print(print("To High! try again!"))
        else:
            print(f"Correct the answer was {answers}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid Guess")
        print(f"Please Select a number Between {lowest_num} and {highest_num}")