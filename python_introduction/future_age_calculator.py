# Create a file named future_age_calculator.py.
# Prompt the user to input their current age with the question: “How old are you? ”.
# Assume the user will input a valid integer value.
# Calculate how old the user will be in the year 2050. To keep calculations simple, assume the current year is 2023. Therefore, you need to add 27 years to the user’s current age.
# Print the user’s age in 2050 in the format: In 2050, you will be [age] years old.

#taking user input 
current_age = int(input("How old are you? "))

#Calculating how old the user will be assuming it is 2023{+27}
future_age = current_age + 27

#display the users age in future
print("In 2050, you will be %d years old" % (future_age))