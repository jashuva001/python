def write_file(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    path = "example.txt"
    write_file(path, "Hello from file_io_example.py\n")
    print("Wrote to file. Contents:")
    print(read_file(path))

if __name__ == "__main__":
    main()