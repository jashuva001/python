import re

def is_palindrome(s):
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

def main():
    s = input("Enter text: ")
    print("Palindrome" if is_palindrome(s) else "Not a palindrome")

if __name__ == "__main__":
    main()