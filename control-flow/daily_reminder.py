#program reminds the user about a single, priority task for the day based on time sensitivity
task = input('Enter your task: ').strip().lower()
priority = input('Priority (high/medium/low): ').strip().lower()
time_bound = input('Is it time-bound? (yes/no): ').strip().lower()

#match case based on priority
match priority:
    case "high":
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print("Note: '{task}' is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print("Note: '{task}' is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound != 'yes':
            print("Note: '{task}' is a low priority task. Consider completing it when you have free time.")

