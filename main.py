import random

print("A game where a computer generates a random number and you have to guess it in a range of 0-10. You have 3 chances!")
number = random.randint(1,10)

attempts_counter = 1
total_Attempts = 3
incorrects = 0

while attempts_counter <= total_Attempts:
    try:
        num = int(input(f"Attempt {attempts_counter}: "))
        attempts_counter+=1
        
        if num == number:
            print(f"Correct! It was {number}!")
            break

        elif num != number: 
            print("Incorrect!")
            incorrects+=1

        if incorrects == 3:
            print(f"Game Over! Correct Answer was {number}!")
    except:
        print("Please put an integer value.")
