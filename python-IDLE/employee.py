class Employee:
     def __init__(self, name, age):
          
          self.name = name
          self.age=age
          
     def displayEmployee(self):
           print "Name : ", self.name
           print "Age : ", self.age

if __name__ == "__main__":
    choice= True
    l=list()
    while choice:
        print ("""
        1.Add items
        2.Delete items
        3.Exit        
        """)
        choice=raw_input("What would you like to do? ") 
        if choice=="1":
             name=raw_input("enter name : ")
             age=raw_input("enter age : ")
             emp1=Employee(name,age)
             l.append(emp1)
             
        elif choice=="2":   
            
            for item in l:
                item.displayEmployee()
            
        elif choice=="3":
             exit()
        else:
            print("\n Not Valid Choice Try again") 
