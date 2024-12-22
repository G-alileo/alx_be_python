
# Generate and Print the Multiplication Table:

# Use a for loop to iterate through the numbers 1 to 10.
# For each iteration, calculate the product of the user’s number 
# and the iterator (the current number in the loop from 1 to 10).
# Print each line of the multiplication table in the format: “X * Y = Z”, 
# where X is the user’s number, Y is the current number in the loop, and Z is the product.

# Prompt User for a Number:
number = int(input("Enter a number to see its multiplication table:"))

# Generate and Print the Multiplication Table:
for Y in range(1,11):
    print("%d * %d = %d" %(number , Y, (number * Y)))

