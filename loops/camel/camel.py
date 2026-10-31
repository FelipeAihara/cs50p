def main():
    variable = input("camelCase: ")

    variable = convert_to_snake_case(variable)
    print(variable)


# Takes a string in camel case and returns a string in snake case
def convert_to_snake_case(s):
    snake_case = ""

    for char in s:
        if char.isupper():
            snake_case = snake_case + "_" + char.lower()
        else:
            snake_case = snake_case + char

    return snake_case

main()