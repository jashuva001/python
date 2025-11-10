def fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def main():
    try:
        n = int(input("How many Fibonacci numbers? "))
        if n < 0:
            raise ValueError("n must be >= 0")
        print(fibonacci(n))
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()