import random

def main():
    target = random.randint(1, 100)
    print("Guess a number between 1 and 100.")
    attempts = 0
    while True:
        try:
            attempts += 1
            guess = int(input("Your guess: "))
            if guess < target:
                print("Too low.")
            elif guess > target:
                print("Too high.")
            else:
                print(f"Correct! Attempts: {attempts}")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()