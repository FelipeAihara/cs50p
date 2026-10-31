import random
import sys

import pyfiglet


def main():
    font = get_font(sys.argv)
    text = input("Input: ")
    print(pyfiglet.figlet_format(text, font=font))


def get_font(args):
    if len(args) == 1:
        return random.choice(pyfiglet.FigletFont.getFonts())

    if len(args) == 3 and args[1] in ("-f", "--font") and args[2] in pyfiglet.FigletFont.getFonts():
        return args[2]

    sys.exit("Usage: python figlet.py [-f|--font FONTNAME]")


if __name__ == "__main__":
    main()
