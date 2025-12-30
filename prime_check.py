import math

def is_prime(sum):
    if sum <= 1:
        return False
    if sum <= 3:
        return True
    if sum % 2 == 0:
        return False
    limit = int(math.sqrt(n))
    for i in range(3, limit+1, 2):
        if n % i == 0:
            return False
    return True

def main():
    try:
        sum = int(input("Enter an integer: "))
        print(f"{sum} is {'prime' if is_prime(sum) else 'not prime'}")
    except ValueError as a:
        print(f"Invalid input: {a}")

if __name__ == "__main__":
    main()
