####Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result
##n=5
##s=lambda x:x+15
##
##print(s(n))
##t=lambda x,y:x*y
##print(t(3,4))
##===============
##Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
n=4
r=lambda x:x*n
print(r(3))
##OR
## creeate a function in which we pass argument of a number and in this we create a lambda function mutliplied by the patrameter of the lambda function and main function argument
##def random_number(n):
##    return lambda x:x*n
##result= random_number(2)
##print("double the number is :",result(3))
##====================================
##. Write a Python program to sort a list of tuples using Lambda.
##Original list of tuples:
##alist=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
##alist.sort(key=lambda x:x[1])## it will take tuple second element 
##print(alist)
##alist.sort(key=lambda x:len(x[0]))#it will take first element of tuple i.e strings 
##print(alist)
###here key is use for 
## Write a Python program to sort a list of dictionaries using Lambda.
##lst=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
##s=sorted(lst,key=lambda x:x['color'])
##print(s)|

