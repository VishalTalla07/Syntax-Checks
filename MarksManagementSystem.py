studentName = input("enter your name: ")
mathsMarks = int(input("enter Maths Marks: "))
scienceMarks = int(input("enter Science Marks: "))
finaceMarks = int(input("enter Finance Marks: "))

def average(mathsMarks, scienceMarks, finaceMarks):
    total = mathsMarks + scienceMarks + finaceMarks
    return total / 3

avg = average(mathsMarks, scienceMarks, finaceMarks)

print("Student Name:", studentName)
print("Average Marks:", avg)

if avg >= 40:
    print("Exam Pass")

    if avg >= 75:
        print("Grade: A")
    elif avg >= 60:
        print("Grade: B")
    else:
        print("Grade: C")
else:
    print("Exam Fail")
