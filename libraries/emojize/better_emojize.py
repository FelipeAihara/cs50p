import emoji


def main():
    text = input("Input: ")
    print("Output:", emojize(text))


def emojize(text):
    text = emoji.emojize(text, language="en")
    text = emoji.emojize(text, language="alias")
    return text


if __name__ == "__main__":
    main()
