import re

def is_palindrome(M):
    cleaned = re.sub(r'[^A-Za-z0-9]', '', M).lower()
    return cleaned == cleaned[::-1]

def main():
    M = input("Enter text: ")
    if is_palindrome(M):
        print("Palindrome")
    else:
        print("Not a palindrome")

if __name__ == "__main__":
    main()
