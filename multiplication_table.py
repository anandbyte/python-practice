"""
Multiplication Table Generator
--------------------------------
Prints the multiplication table (1 to 10) for a number entered by the user.
"""


def print_table(number: int, upto: int = 10) -> None:
    """Print the multiplication table of `number` from 1 to `upto`."""
    for i in range(1, upto + 1):
        print(f"{number} x {i} = {number * i}")


def get_number() -> int:
    """Prompt the user until a valid integer is entered."""
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a whole number (e.g., 5).")


def main() -> None:
    number = get_number()
    print_table(number)


if __name__ == "__main__":
    main()
