#Taking user values
task = input("Enter your task: ")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "low":
        if time_bound == "yes":
            print("Reminder: %s is a low priority task that requires immediate attention today!" %(task))
        else:
            print("Note: %s is a low priority task. Consider completing it when you have free time." %(task))
    case "medium":
        if time_bound == "yes":
            print("Reminder: %s is a medium priority task that requires immediate attention today!" %(task))
        else:
            print("Note: %s is a medium priority task. Consider completing it when you have free time." %(task))
    case "high":
        if time_bound == "yes":
            print("Reminder: %s is a high priority task that requires immediate attention today!" %(task))
        else:
            print("Note: %s is a high priority task. Consider completing it when you have free time." %(task))