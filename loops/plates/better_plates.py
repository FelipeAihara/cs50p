def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False

    if not s[:2].isalpha():
        return False

    numbers_started = False

    for char in s[2:]:
        if char.isdigit():
            if not numbers_started and char == "0":
                return False
            numbers_started = True
        elif char.isalpha():
            if numbers_started:
                return False
        else:
            return False

    return True


if __name__ == "__main__":
    main()
