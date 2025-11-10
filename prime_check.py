import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.sqrt(n))
    for i in range(3, limit+1, 2):
        if n % i == 0:
            return False
    return True

def main():
    try:
        n = int(input("Enter an integer: "))
        print(f"{n} is {'prime' if is_prime(n) else 'not prime'}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()