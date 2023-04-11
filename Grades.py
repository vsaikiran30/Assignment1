Marks = int(input("Enter the marks : "))
if Marks < 25:
    grade = ("F")
elif Marks >= 25 and Marks < 45:
    grade = ("E")
elif Marks >= 45 and Marks < 50:
    grade = ("D")
elif Marks >= 50 and Marks < 60:
    grade = ("C")
elif Marks >= 60 and Marks < 80:
    grade = ("B")
else: 
    grade = ("A") 
print ( "Grade: ",grade)