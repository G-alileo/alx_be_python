# Prompt User for a Number:
number = int(input("Enter a number to see its multiplication table:"))

# Generate and Print the Multiplication Table:
for Y in range(1,11):
    print("%d x %d = %d" %(number , Y, (number * Y)))

