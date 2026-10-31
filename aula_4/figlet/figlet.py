import sys
import pyfiglet
import random

def main():
    fonts = pyfiglet.FigletFont.getFonts()
    
    RANDOM = 1
    SELECTED = 2

    if (len(sys.argv) == 3):
        if (sys.argv[1] not in ("-f", "--font")):
            sys.exit("sys.argv[1] is not int (\"-f\", \"--font\"")
        elif (sys.argv[2] not in fonts):
            sys.exit("sys.argv[2] not in fonts")
        n = SELECTED
    elif (len(sys.argv) == 1):
        n = RANDOM
    else:
        sys.exit("Length of command line arguments is not equal 1 or 3")

    text = input("Input: ")

    match n:
        case 1:
            print(pyfiglet.figlet_format(text, font=random.choice(fonts)))

        case 2:
            print(pyfiglet.figlet_format(text, font=sys.argv[2]))

if __name__ == "__main__":
    main()
