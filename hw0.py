#user input:input the polynomial
user_input=input("Input the polynomials:")

#Split the polynomial into sublists according to the operators
user_add=user_input.split("+")
if user_add.find(X)==2:  #AttributeError: 'list' object has no attribute 'find'
	user_p2.append(1)
elif user_p2.find(X)==-1:
	user_p2.insert(0,1)
	user_p2.append(1)
elif user_p2.find(X)==0:
	user_p2.insert(0,1)
	user_p2.append(1)	


#Split the sublists by mulplication 
user_p3=user_p2.split("*")

#Split the sublists by power
user_p4=user_p3.split("^")

#Calculate the value of polynomial
x=int(user_x)
