"""
GradeBook Analyzer
Course: Programming for Problem Solving using Python
Student: <Your Pravindra Singh>
Date: 2025
Description: CLI tool to input student marks, analyze grades, and print summary.
"""

import csv
import statistics





def calculate_average(marks):
    return sum(marks.values()) / len(marks)

def calculate_median(marks):
    
    return statistics.median(marks.values())

def find_max_score(marks):
    return max(marks.values())

def find_min_score(marks):
    return min(marks.values())


def assign_grades(marks):
    grades = {}
    for student, score in marks.items():
        if score >= 90:
            grades[student] = "A"
        elif score >= 80:
            grades[student] = "B"
        elif score >= 70:
            grades[student] = "C"
        elif score >= 60:
            grades[student] = "D"
        else:
            grades[student] = "F"
    return grades


def export_to_csv(marks, grades):
    with open("grade_report.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Marks", "Grade"])
        for name in marks:
            writer.writerow([name, marks[name], grades[name]])
    print("\n✅ Grade report exported as grade_report.csv\n")


def get_manual_input():
    marks = {}
    count = int(input("Enter number of students: "))
    for _ in range(count):
        name = input("Enter student name: ")
        score = int(input(f"Enter marks for {name}: "))
        marks[name] = score
    return marks

def load_csv():
    marks = {}
    filename = input("Enter CSV file name: ")
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            marks[row[0]] = int(row[1])
    print("\n✅ CSV Loaded Successfully\n")
    return marks


def print_table(marks, grades):
    print("\nName\t\tMarks\tGrade")
    print("-" * 30)
    for name in marks:
        print(f"{name:<15}{marks[name]:<10}{grades[name]}")
    print("-" * 30)


def main():
    print("📘 Welcome to GradeBook Analyzer 📘")

    while True:
        print("""
Choose Input Method:
1. Manual Entry
2. Load from CSV
3. Exit
""")
        choice = input("Enter your choice: ")

        if choice == "1":
            marks = get_manual_input()
        elif choice == "2":
            marks = load_csv()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid input. Try again.")
            continue

        avg = calculate_average(marks)
        med = calculate_median(marks)
        highest = find_max_score(marks)
        lowest = find_min_score(marks)

        grades = assign_grades(marks)


        passed = [s for s in marks if marks[s] >= 40]
        failed = [s for s in marks if marks[s] < 40]

        print_table(marks, grades)

        print(f"\n📊 Statistics:")
        print(f"Average Marks: {avg:.2f}")
        print(f"Median Marks: {med}")
        print(f"Highest Score: {highest}")
        print(f"Lowest Score: {lowest}")

        distribution = {g: list(grades.values()).count(g) for g in "ABCDF"}
        print("\n🎯 Grade Distribution:")
        for g in distribution:
            print(f"{g}: {distribution[g]}")

        print(f"\n✅ Passed: {len(passed)} -> {passed}")
        print(f"❌ Failed: {len(failed)} -> {failed}")

        save = input("\nSave results as CSV? (y/n): ")
        if save.lower() == "y":
            export_to_csv(marks, grades)

        repeat = input("\nRun again? (y/n): ")
        if repeat.lower() != "y":
            print("\nThank you! 👋")
            break

if __name__ == "__main__":
    main()
