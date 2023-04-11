TotalClasses_held = int(input("Total Classes held: "))
Classes_attended = int(input("Classes attended: ")) 
attendence_percentage = (Classes_attended/TotalClasses_held)*100 
if attendence_percentage >= 75:
    print("Attendence_percentage:",attendence_percentage)
    print("Student is allowed to sit in exam")
else:
    print("Attendence_percentage:",attendence_percentage)
    print("Student is not allowed to sit in exam")
