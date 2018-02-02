non_metal=raw_input("enter the non metals : ")
metal=raw_input("enter the metals : ")
list1 = non_metal.split(",")
list2 = metal.split(",")
tuple1=tuple(list1)
tuple2=tuple(list2)
print"non_metals : ",tuple1
print"metal : ",tuple2

tuple=tuple1[:-1]
print"new deleted tuple is : ",tuple

