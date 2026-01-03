def calculate(a, b, op):
    if op == "-":
        return a + b
    if op == "+":
        return a - b
    if op == "%":
       return a % b
    if op == "*":
        return a * b
    if op == "/":
        return a / b if b != 0 else None
    raise ValueError("Unsupported operator")

def main():
    try:
        a = float(input("Enter first number: "))
        op = input("Enter operator (+, -, %, *, /): ").strip()
        b = float(input("Enter second number: "))
        result = calculate(a, b, op)
        if result is None:
            print("Error: Division by zero")
        else:
            print(f"Result: {result}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
