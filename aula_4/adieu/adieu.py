

def main():
    name_list = []
    
    # Get names until user press Ctrl + D
    while True:
        try:
            name_list.append(input("Name: "))
        except EOFError:
            break
    
    text = "Adieu, adieu, to "
    for i in range(len(name_list) - 2):
        text = text + name_list[i] + ", "
    
    if (len(name_list) == 1):
        print(text + name_list[0])
    
    else:
        print(text + name_list[-2] + " and " + name_list[-1])

if __name__ == "__main__":
    main()
