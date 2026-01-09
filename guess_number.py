import random

def main():
    target = random.randint(1, 1000)
    print("Guess a number between 1 and 1000.")
    attempts = 0
    while True:
        try:
            
            guess = int(input("Your guess: "))
            if guess < target:
                print("Too low value.")
            elif guess > target:
                print("Too hight value.")
            else:
                print(f"Correct! Attempts: {attempts}")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
