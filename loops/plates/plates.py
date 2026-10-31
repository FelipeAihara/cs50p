def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (len(s) < 2 or len(s) > 6):
        return False

    valid_letters = "abcdefghijlkmnopqrstuvwxyz"
    valid_numbers = "0123456789"
    s = s.strip()
    s = s.lower()

    if (s[0] not in valid_letters or s[1] not in valid_letters):
        return False

    for i, char in enumerate(s[2:], start=2):
        if char in valid_numbers:
            for char in s[i+1:]:
                if char not in valid_numbers:
                    return False 
        elif char not in valid_letters:
            return False

    return True

main()