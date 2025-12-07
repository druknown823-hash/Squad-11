try:
    f = open("example.txt", "r")
    content = f.read()
    print(content)

except FileNotFoundError:
    print("File does not exist!")

except Exception as e:
    print("Some error occurred:", e)

finally:
    print("Closing file...")
    try:
        f.close()
    except:
        print("File was never opened.")
