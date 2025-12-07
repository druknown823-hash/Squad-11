try:
    file=open('example.txt', 'r')
    content=file.read()
    print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
finally:
    if 'file' in locals():
        file.close()
#read file line by line using rereadline
with open('example.txt', 'r') as file:
    line1 = file.readline()
    line2 = file.readline()
    print("First line:", line1)
    print("Second line:", line2)
