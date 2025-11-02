# Guess the number game in python

import random # to generate random number

lowest_num = 1
highest_num = 100
guesses = 0
is_running = True

answer = random.randint(lowest_num,highest_num) # randint method taking two arguments lowest num and highest num

print('Welcome to \nNumber Guessing Game')
print(f'Select no. between {lowest_num} and {highest_num}')

# main logic
while is_running:

    guess = int(input("Enter your guess :"))
    if guess.isdigit():
        guess = int(guess)
        guess += 1

        if guess < lowest_num or guess > highest_num:
            print('You entered no. outside of he range {lowest_num} and {highest_num}')
        
        elif guess < answer:
            print("Too low ! Try high number")

        elif guess > answer:
            print("Too high ! Try low")

        else:
            print("Congrats ! The answer is {answer}")
            print("Total guesses :{guesses}")

    
    else:
        print('Invalid guess')
        print(f'Select no. between {lowest_num} and {highest_num}')
