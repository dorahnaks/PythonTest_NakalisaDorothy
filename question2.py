# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F

student_mark = int(input("Enter your marks: "))

if student_mark >= 90:
    print(f"{student_mark} is Grade A")
elif student_mark >= 80:
    print(f"{student_mark} is Grade B")
elif student_mark >= 70:
    print(f"{student_mark} is Grade C")
elif student_mark >= 60:
    print(f"{student_mark} is Grade D")
elif student_mark >= 40:
    print(f"{student_mark} is Grade E")
else:
    print(f"{student_mark} is Grade F")