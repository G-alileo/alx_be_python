# Prompt User for a Number:
number = int(input("Enter a number to see its multiplication table:"))

# Generate and Print the Multiplication Table:
for Y in range(1,11):
    Z = "%d * %d = %d" %(number , Y, (number * Y))
    print(Z)

