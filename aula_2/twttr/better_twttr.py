def main():
    inp = input("Input: ")

    out = omit_vowels(inp)
    print(f"Output: {out}")


# Takes a string and returns the same string, but omitting the vowels
def omit_vowels(s):
    no_vowels = []
    vowels = "aeiou"

    for char in s:
        if char.lower() not in vowels:
            no_vowels.append(char)

    return "".join(no_vowels)


if __name__ == "__main__":
    main()
