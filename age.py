a = int(input("Age of first person : "))
b = int(input("Age of second person : "))
c = int(input("Age of third person : ")) 
if a>b:
    older = a 
    younger = b 
elif b>c:
    older = b 
    younger = c 
elif c>a:
    older = c 
    younger = a
print("Older:",older)
print("Younger:",younger)