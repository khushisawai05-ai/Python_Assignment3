# Find the student who has scored the highest marks.
students ={"Rahul":78,"Amit":92,"Priya":85}
highest_marks = max(students.values())
for name,marks in students.items():
    if marks==highest_marks:
        print("Highest Marks:",highest_marks)
        print("Student:",name)
