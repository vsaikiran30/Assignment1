salary = int(input("Enter the amount :"))
service = int(input("Enter the service :"))
if service > 5:
    bonus = 0.05 * salary
    print(bonus) 
else:
    print("No Bonus")