employee=[]

while True:
    choice=input('want to enter the detail:')
    choice=choice.lower()
    if(choice=="yes"):
        fname,lstName=input("enter the name:").split()
        employee.append({"fname":fname,"lstname":lstName})
        
    else:
        print("detailed")
        break
        

print(employee)
