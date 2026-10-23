expression = input("Expression: ")
arguments = expression.split()
match arguments[1]:
    case "+":
        print(f"{(int(arguments[0]) + int(arguments[2])):.1f}")
    case "-":
        print(f"{(int(arguments[0]) - int(arguments[2])):.1f}")
    case "*":
        print(f"{(int(arguments[0]) * int(arguments[2])):.1f}")
    case "/":
        print(f"{(int(arguments[0]) / int(arguments[2])):.1f}")