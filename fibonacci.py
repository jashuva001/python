def fibonacci(num):
    seq = []
    x, y = 0, 1
    for _ in range(num):
        seq.append(x)
        x, y = y, x + y
    return seq

def main():
    try:
        num = int(input("How many Fibonacci numbers? "))
        if num < 0:
            raise ValueError("num must be >= 0")
        print(fibonacci(num))
    except ValueError as error:
        print(f"Invalid input: {error}")

if __name__ == "__main__":
    main()
