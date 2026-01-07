def write_file(path: str, text: str) -> None:
    """Write text to a file, overwriting if it exists."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def read_file(path: str) -> str:
    """Read and return the contents of a file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def main() -> None:
    path = "example.txt"

    try:
        write_file(path, "Hello from file_io_example.py\n")
        print("Wrote to file. Contents:")
        contents = read_file(path)
        print(contents)
    except OSError as e:
        print(f"File error occurred: {e}")


if __name__ == "__main__":
    main()
