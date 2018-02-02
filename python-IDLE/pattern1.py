n=int(input("enter the limit :"))
for i in range(0, n):   # check i<n
	for j in range(0, i+1): #check j<i+1
		print("* ",end="")
	print()


# end=""  : print("hello"); print("hi")
#   outpit :hello
#           hi

# end=""  : print("hello",end=" "); print("hi")
#   outpit :hello hi

# print()  : print a new line
