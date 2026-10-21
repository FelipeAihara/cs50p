def main():
    input_string = input("Enter a string containing the substring :) or :( : ")
    input_string = convert(input_string)
    print(input_string)

def convert(string):
    string = string.replace(":)", "🙂").replace(":(", "🙁")
    return string

if __name__ == "__main__":
    main()