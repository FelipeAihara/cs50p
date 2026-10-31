def main():
    inp = input("Input: ")

    out = omit_vowells(inp)
    print(f"Output: {out}")

# Takes a string and returns the same string, but omitting the vowels
def omit_vowells(s):
    no_vowells = []
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for char in s:
        if char not in vowels:
            no_vowells.append(char)

    return "".join(no_vowells)


if __name__ == "__main__":
    main()