1.String:-
name = "xyz"
department = "Computer Science"
address = "Ahilyanagar"
email = abc@gmail.com

name = input("Enter student name: ")
department = input("Enter department: ")
print("name:", name)
print(“department:”, department)

2.List:-
subjects = ["Python", "Maths", "Physics"]
marks = [80, 75, 90]
attendance = [85, 90, 80]

print("Subjects:", subjects)
print("Marks:", marks)
print("Attendance:", attendance)

3.Tuple:-
Roll number = (101,)
Registration number = ("REG2026CS101",)
Date of birth = ("15-08-2007",)

print("Roll Number:", Roll number)
print("Registration Number:", Registration number)
print("Date of Birth:", Date of birth)

4.Sets
departments = {"Computer Science", "Mechanical", "Civil"}
subjects = {"Python", "Maths", "Physics"}
clubs = {"NSS", "Sports", "Coding Club"}

print("Departments:", departments)
print("Subjects:", subjects)
print("Student Clubs:", clubs)

5.Dictionaries
student = {
    "roll number": 101,
    "name": "Rahul",
    "department": "Computer Science",
    "subjects": ["Python", "Maths", "Physics"],
    "marks": [80, 75, 90],
    "attendance": [85, 90, 80],
    "contact": "9876543210"
}

print("Student Record")
print("Roll Number:", student["roll number"])
print("Name:", student["name"])
print("Department:", student["department"])
print("Subjects:", student["subjects"])
print("Marks:", student["marks"])
print("Attendance:", student["attendance"])
print("Contact:", student["contact"])
