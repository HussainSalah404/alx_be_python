# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        priority_msg = "This task is of HIGH priority."
    case "medium":
        priority_msg = "This task is of medium priority."
    case "low":
        priority_msg = "This task is of low priority."
    case _:
        priority_msg = "The priority of this task is unknown."

if time_bound == "yes":
    urgency_msg = "Since it is time-sensitive, immediate action is required."
else:
    urgency_msg = "This task is not time-sensitive."

print(f"Reminder: '{task}'. {priority_msg} {urgency_msg}")