# Create a file named hours_to_seconds.py.
# Define a variable named hours and assign it a value representing the number of hours you want to convert to seconds. Use hours = 2.
# Calculate the number of seconds in the given hours. Remember, there are 3600 seconds in an hour (since there are 60 minutes in an hour and 60 seconds in a minute, thus 60 x 60 = 3600).
# Store the result of the conversion in a variable named seconds.
# Print the result in the format: [hours] hour(s) is [seconds] seconds.

#defining variables
hours = 2

#calculating the number of seconds in the given hours
seconds = hours * 3600

#display the results
print(hours,"hour(s) is " + str(seconds) )