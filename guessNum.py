# Guess the number game in python

import random  # to generate random number

lowest_num = 1
highest_num = 100
guesses = 0
is_running = True

answer = random.randint(lowest_num, highest_num)

print('🎯 Welcome to Number Guessing Game!')
print(f'Select a number between {lowest_num} and {highest_num}')

# main logic
while is_running:
    guess_input = input("Enter your guess: ")

    if guess_input.isdigit():
        guess = int(guess_input)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print(f'⚠️ You entered a number outside the range {lowest_num} and {highest_num}')
        elif guess < answer:
            print("🔼 Too low! Try a higher number.")
        elif guess > answer:
            print("🔽 Too high! Try a lower number.")
        else:
            print(f"✅ Congrats! The answer was {answer}.")
            print(f"🎉 You guessed it in {guesses} attempts!")
            is_running = False
    else:
        print(f'❌ Invalid input. Please enter a number between {lowest_num} and {highest_num}.')
