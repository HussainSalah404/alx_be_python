task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        base_reminder = f"The task '{task}' is HIGH priority."
    case "medium":
        base_reminder = f"The task '{task}' is medium priority."
    case "low":
        base_reminder = f"The task '{task}' is low priority."
    case _:
        base_reminder = f"The task '{task}' has an unknown priority."

if time_bound == "yes":
    full_reminder = f"{base_reminder} It is time-sensitive and needs immediate attention!"
else:
    full_reminder = f"{base_reminder} It is not time-sensitive."

print("\n" + full_reminder)
