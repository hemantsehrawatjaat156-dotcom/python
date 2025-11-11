# -------------------------------------------------------------
# Project Title : Daily Calorie Tracker CLI
# Author        : [Hemant singh sehrawat]
# Date          : [08/11/2025]

# -------------------------------------------------------------

print("==========================================")
print(" Welcome to the Daily Calorie Tracker CLI ")
print("==========================================")
print("This tool helps you log meals, track calories,")
print("and compare your total intake with your daily limit.\n")

meal_names = []
calorie_values = []

num_meals = int(input("How many meals would you like to log today? "))

for i in range(num_meals):
    meal = input(f"Enter the name of meal {i + 1}: ")
    calories = float(input(f"Enter calories for {meal}: "))
    meal_names.append(meal)
    calorie_values.append(calories)

print("\nData successfully recorded!\n")

total_calories = sum(calorie_values)
average_calories = total_calories / len(calorie_values)

daily_limit = float(input("Enter your daily calorie limit: "))

if total_calories > daily_limit:
    limit_status = "Warning: You have exceeded your daily calorie limit!"
else:
    limit_status = "Great! You are within your daily calorie limit."

print("\n==========================================")
print("          Daily Calorie Summary           ")
print("==========================================")
print(f"{'Meal Name':<15}{'Calories'}")
print("------------------------------------------")

for meal, cal in zip(meal_names, calorie_values):
    print(f"{meal:<15}{cal:.2f}")

print("------------------------------------------")
print(f"{'Total:':<15}{total_calories:.2f}")
print(f"{'Average:':<15}{average_calories:.2f}")
print("==========================================")
print(limit_status)
print("==========================================\n")

save_option = input("Would you like to save this session to a file? (y/n): ").lower()

if save_option == 'y':
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "calorie_log.txt"

    with open(filename, "a") as file:
        file.write("==========================================\n")
        file.write(f"Calorie Tracker Log - {timestamp}\n")
        file.write("==========================================\n")
        for meal, cal in zip(meal_names, calorie_values):
            file.write(f"{meal:<15}{cal:.2f}\n")
        file.write("------------------------------------------\n")
        file.write(f"Total: {total_calories:.2f}\n")
        file.write(f"Average: {average_calories:.2f}\n")
        file.write(f"Limit: {daily_limit:.2f}\n")
        file.write(limit_status + "\n")
        file.write("==========================================\n\n")

    print(f"\n Session successfully saved to '{filename}'!\n")
else:
    print("\n Session not saved. Goodbye!\n")


print("Thank you for using the Daily Calorie Tracker CLI!")

