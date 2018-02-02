x = raw_input("Input list 1 : ")
y = raw_input("Input list 2 : ")
a=list(set(x)-set(y))
b=list(set(y)-set(x))
print"difference between list 1 and 2 : ",a
print"difference between list 2 and 1 : ",b
list1=a+b
print"result : ",list1
