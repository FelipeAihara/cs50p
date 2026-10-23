file = input("File name: ")
file = file.strip().lower()

if (file.endswith(".gif")):
    print("image/gif")
elif (file.endswith((".jpg", ".jpeg"))):
    print("image/jpeg")
elif (file.endswith(".png")):
    print("image/png")
elif (file.endswith(".pdf")):
    print("applicaiton/pdf")
elif (file.endswith(".txt")):
    print("text/txt")
elif (file.endswith(".zip")):
    print("folder/zip")
else:
    print("application/octet-stream")
