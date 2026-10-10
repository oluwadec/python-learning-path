"""05_nested_data.py - Lists and dictionaries inside each other."""

school = {
    "name": "Greenfield High",
    "students": [
        {"name": "Ada", "grades": [90, 85, 92]},
        {"name": "Ben", "grades": [70, 65, 80]},
        {"name": "Chi", "grades": [88, 91, 79]},
    ],
}

# Reach into the structure step by step
print("First student:", school["students"][0]["name"])

# Loop through the students and calculate averages
for student in school["students"]:
    average = sum(student["grades"]) / len(student["grades"])
    print(f"{student['name']}: average {average:.1f}")

# Add a new student
school["students"].append({"name": "Dayo", "grades": [95, 97]})
print("Number of students:", len(school["students"]))

# Collect every grade into one list
all_grades = [g for s in school["students"] for g in s["grades"]]
print("Highest grade overall:", max(all_grades))
