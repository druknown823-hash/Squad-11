filename = input("Enter file name to read: ")

try:
    with open(filename, "r") as file:
        data = file.read()
        print("File content:\n", data)

except FileNotFoundError:
    print("Error: File not found!")

except PermissionError:
    print("Error: You do not have permission to read this file.")

except Exception as e:
    print("Some other error occurred:", e)
