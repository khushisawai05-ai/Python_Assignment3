# Create a Python program that uses functions to calculate a student's result.
def calculate_total(marks):
    return sum(marks)
def calculate_percentage(total):
    return total/5
def determine_grade(percentage):
    if percentage >=90:
        return "A"
    elif percentage >=80:
        return "B"
    elif percentage >=70:
        return "C"
    elif percentage >=60:
        return "D"
    else:
        return "F"
def determine_result(percentage):
    if percentage >=40:
        return "Pass"
    else:
        return "Fail"
python = int(input("Enter marks for Python:"))
maths = int(input("Enter marks for Maths:"))
database = int(input("Enter marks for database:"))
networks = int(input("Enter marks for Networks:"))
ai = int(input("Enter marks for AI:"))
marks =[python,maths,database,networks,ai]
# Function calls
total = calculate_total(marks)
percentage = calculate_percentage(total)
grade = determine_grade(percentage)
result = determine_result(percentage)

# Display result
print("Total Marks:",total)
print("Percentage:",percentage)
print("Grade:",grade)
print("Result:",result)