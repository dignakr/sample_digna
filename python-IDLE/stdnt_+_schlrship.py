class Student:
    
    def __init__(self, rollno, name, dob, age, mark):
        self.rollno=rollno
        self.name=name
        self.dob=dob
        self.age=age
        self.mark=mark

    def displayStudent(self):
        for i in range(0,limit):
            print "Roll No : ",self.rollno
            print "Name : ", self.name
            print "DOB : ", self.dob
            print "Age : ", self.age
            print "Mark : ", self.mark

    def delete(self):
         c=raw_input("which item to delete? ")
         for i in l:
                if i.self.name==c:
                    #k=l.index(i)
                    l.remove(i)
                    print'This student is deleted successfully'


if __name__ == "__main__":

    ans=True
    l=list()
    
    while ans:
            print ("""
                1.Add student
                2.View student
                3.Delete student
                4.Enroll for scholarship
                5.View all scholarship details
                6.Exit/Quit           
                """)
            
            ans=raw_input("What would you like to do? ")
            if ans=="1":
                 
                 print "Enter the number of students : "
                 limit = input()
                 for i in range(0,limit):
                    rollno=raw_input("enter the roll no : ")
                    name=raw_input("enter the name : ")
                    dob=raw_input("enter the dob : ")
                    age=raw_input("enter the age : ")
                    std1=Student(rollno, name, dob, age, mark)

                    for item in range(0,3):
                        x=input("enter the marks :")
                        l.append(x)                
                
                
            elif ans=="2":
                for i in l:
                
                    i.displayStudent()

            elif ans=="3":
                    std1.delete()
            
            elif ans=="5":
                print("\n bye") 
                exit()
       
            else:
              print("\n Not Valid Choice Try again") 
       



















                
            
