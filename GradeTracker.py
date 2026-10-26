# 33th github project --> Grade Tracker
print('----------Grade Tracker----------')
grades = {}


def show_grades():
    if not grades:
        print("No grades yet.")
        return
    for name, score in grades.items():
        print(f"{name}: {score:.1f}")


def add_grade():
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    try:
        score = float(input("Score (0-100): "))
    except ValueError:
        print("Enter a valid number.")
        return
    if not 0 <= score <= 100:
        print("Score must be between 0 and 100.")
        return
    grades[name] = score
    print(f"Added {name}: {score:.1f}")


def show_average():
    if not grades:
        print("No grades yet.")
        return
    avg = sum(grades.values()) / len(grades)
    print(f"Average: {avg:.2f}")
    print(f"Highest: {max(grades.values()):.1f}")
    print(f"Lowest:  {min(grades.values()):.1f}")


def main():
    actions = {
        "1": show_grades,
        "2": add_grade,
        "3": show_average,
    }

    while True:
        print("\n1. View  2. Add  3. Stats  4. Quit")
        choice = input("Choose: ").strip()

        if choice == "4":
            print("Goodbye!")
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice.")

main()