import matplotlib.pyplot as plt
steps_list = []
calories_list = []
goal_steps = 10000


def get_average(values):
    if len(values) == 0:
        return 0
    return sum(values) / len(values)


def get_total(values):
    return sum(values)


def get_best_day(values):
    if len(values) == 0:
        return 0
    return max(values)


def get_bmi(weight_kg, height_m):
    return weight_kg / (height_m * height_m)


def add_record():
    steps_text = input("Steps: ")
    calories_text = input("Calories burned: ")

    try:
        steps = int(steps_text)
        if steps < 0:
            raise ValueError
    except ValueError:
        print("Invalid steps. Enter a non-negative whole number.")
        print("Record not saved.")
        return

    try:
        calories = int(calories_text)
        if calories < 0:
            raise ValueError
    except ValueError:
        print("Invalid calories. Enter a non-negative whole number.")
        print("Record not saved.")
        return

    steps_list.append(steps)
    calories_list.append(calories)
    day = len(steps_list)
    goal_achieved = steps >= goal_steps
    goal_percent = steps / goal_steps * 100
    print(f"Record saved for Day {day}. Goal achieved: {'Yes' if goal_achieved else 'No'}")
    print(f"({goal_percent:.2f}% of goal)")


def show_summary():
    if len(steps_list) == 0:
        print("No records available.")
        return

    average_steps = get_average(steps_list)
    total_calories = get_total(calories_list)
    best_steps = get_best_day(steps_list)
    best_day = steps_list.index(best_steps) + 1
    goal_days = sum(1 for steps in steps_list if steps >= goal_steps)
    print(f"Average steps: {average_steps:.2f} | Total calories: {total_calories} | Best day: Day {best_day} ({best_steps} steps) | Goal days: {goal_days}/{len(steps_list)}")


def show_bmi():
    try:
        weight_kg = float(input("Weight (kg): "))
        height_m = float(input("Height (m): "))
        if weight_kg <= 0 or height_m <= 0:
            print("Weight and height must be positive.")
            return
    except ValueError:
        print("Enter valid numbers for weight and height.")
        return

    bmi = get_bmi(weight_kg, height_m)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    print(f"BMI: {bmi:.2f} | Category: {category}")


def show_chart():
    if len(steps_list) == 0:
        print("No records available.")
        return


    days = list(range(1, len(steps_list) + 1))
    plt.bar(days, steps_list)
    plt.axhline(y=goal_steps, color="red", linestyle="--", label="10000-step goal")
    plt.title("Daily Steps")
    plt.xlabel("Day")
    plt.ylabel("Steps")
    plt.xticks(days)
    plt.legend()
    plt.show()


while True:
    print("\n1. Add record")
    print("2. Summary")
    print("3. BMI")
    print("4. Chart")
    print("5. Exit")
    menu_option = input("Choose an option: ")

    if menu_option == "1":
        add_record()
    elif menu_option == "2":
        show_summary()
    elif menu_option == "3":
        show_bmi()
    elif menu_option == "4":
        show_chart()
    elif menu_option == "5":
        break
    else:
        print("Invalid menu option.")
