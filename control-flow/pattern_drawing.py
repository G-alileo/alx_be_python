# Prompt User for Pattern Size:
size = int(input("Enter the size of the pattern:"))

#Validating user input
if size <= 0:
    print("Enter a positive integer")
else:
    row = 0
    while row < size:
        for column in range(size):
            print("*",end="")
        print()
        row += 1
    