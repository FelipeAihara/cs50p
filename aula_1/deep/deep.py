answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
answer = answer.strip().title()
print(answer)
if answer == "42" or answer == "Forty-Two" or answer == "Forty Two":
    print("Yes")
else:
    print("No")