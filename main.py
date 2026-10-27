students = [
    {"name": "Aung Aung", "score": 85},
    {"name": "Su Su", "score": 92},
    {"name": "Mg Mg", "score": 35}
]

# Function to classify grade
def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 40:
        return "C"
    else:
        return "F"


# 1. Display each student's name and score
print("Student Names and Scores:")
for student in students:
    print(student["name"], "-", student["score"])


# 2. Classify each student's grade using a function
print("\nStudent Grades:")
for student in students:
    grade = get_grade(student["score"])
    print(student["name"], "-", grade)


# 3. Display only passing students (score >= 40)
print("\nPassing Students:")
for student in students:
    if student["score"] >= 40:
        print(student["name"], "-", student["score"])


# 4. Add a fourth student
students.append({"name": "Kyaw Kyaw", "score": 75})

print("\nAfter Adding Fourth Student:")
for student in students:
    print(student["name"], "-", student["score"])


# 5. Create a tuple of three subject names and display them
subjects = ("Python", "Database", "Networking")

print("\nSubjects:")
for subject in subjects:
    print(subject)
