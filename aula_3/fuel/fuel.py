def main():
    percentage = get_percentage()
    print_fuel(percentage)


def get_percentage():
    while True:
        try:
            fraction = input("Fraction: ")
            x = int(fraction[0:fraction.index("/")])
            y = int(fraction[fraction.index("/")+1:])
        except ValueError or ZeroDivisionError:
            pass
        else:
            if (x <= y and x >= 0):
                return int(100 * x / y)

def print_fuel(p):
    if p <= 1:
        print("E")
    elif p >= 99:
        print("F")
    else:
        print(f"{p}%")

if __name__ == "__main__":
    main()
