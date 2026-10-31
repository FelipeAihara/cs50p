def main():
    percentage = get_percentage()
    print_fuel(percentage)


def get_percentage():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x, y = int(x), int(y)
            if y == 0:
                raise ZeroDivisionError
        except (ValueError, ZeroDivisionError):
            continue
        else:
            if 0 <= x <= y:
                return round(100 * x / y)


def print_fuel(p):
    if p <= 1:
        print("E")
    elif p >= 99:
        print("F")
    else:
        print(f"{p}%")


if __name__ == "__main__":
    main()
