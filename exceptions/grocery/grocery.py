def main():
    gl = get_grocery_list()
    print_grocery_list(gl)


def get_grocery_list():
    gl = {}

    while True:
        try:
            item = input("").upper()
            
            if item not in gl.keys():
                gl[item] = 1
            else:
                gl[item] += 1

        except EOFError:
            print("")
            return dict(sorted(gl.items()))


def print_grocery_list(gl):
    items = gl.keys()
    for item in gl:
        print(f"{gl[item]} {item}")

if __name__ == "__main__":
    main()
