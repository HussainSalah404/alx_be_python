task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high" | "medium" | "low":
        print(f"'{task}' is a {priority.upper()} priority task.", end=" ")
    case _:
        print(f"'{task}' has an unknown priority.", end=" ")

if time == "yes":
    print("It requires immediate attention today!")
else:
    print()