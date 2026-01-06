def factorial(a):
    if a < 0:
        raise ValueError("a must be >= 0")
    result = 1
    for i in range(2, a+1):
        result *= i
    return result

def main():
    try:
        a = int(input("Enter a non-negative integer: "))
        print(f"{a}! = {factorial(a)}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
