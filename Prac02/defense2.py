students = {
    "id1": 100,
    "id2": 80,
    "id3": 0
}

for student_id, points in students.items():
    if 90 <= points <= 100:
        gpa = 4.0
    elif 80 <= points < 90:
        gpa = 3.8
    else:
        gpa = 0

    print(student_id, "GPA ", gpa)

