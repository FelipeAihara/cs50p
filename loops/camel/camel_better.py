def main():
    variable = input("camelCase: ")
    print(convert_to_snake_case(variable))


# Takes a string in camel case and returns a string in snake case
def convert_to_snake_case(s):
    letters = []

    for char in s:
        if char.isupper():
            letters.append("_")
            letters.append(char.lower())
        else:
            letters.append(char)

    return "".join(letters)


if __name__ == "__main__":
    main()
