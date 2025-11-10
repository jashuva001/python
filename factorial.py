def factorial(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def main():
    try:
        n = int(input("Enter a non-negative integer: "))
        print(f"{n}! = {factorial(n)}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()