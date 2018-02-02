
class Student:
    
    def __init__(self, rollno, name, dob, age, mark):
        self.rollno=rollno
        self.name=name
        self.dob=dob
        self.age=age
        self.mark=mark
        

    def displayStudent(self):
        print "Roll No : ",self.rollno
        print "Name : ", self.name
        print "DOB : ", self.dob
        print "Age : ", self.age
        print "Mark : ", self.mark 
       
    def add(self):
        
        s=self.mark[0]+self.mark[1]+self.mark[2]+self.mark[3]+self.mark[4]
        return s
    def avg(self):
        av=std1.add()/5
        return av
    def calculategrade(self):
        if std1.add()/500>0.8:
            print("Your grade is distinction")
        elif std1.add()/500.0>0.6:
            print"Your grade is first class"
        elif std1.add()/500.0>0.4:
            print"Your grade is second class"
        else:
             print"fail"

    def scholarship(self):
        if std1.add()/500.0>=0.9:
            print  "you are eligible for scholarship"
        else:
            print "Not eligible for scholarship"
            
if __name__ == "__main__":
        print "Enter the number of students : "
        limit = input()
        for i in range(0,limit):
            rollno=raw_input("enter the roll no : ")
            name=raw_input("enter the name : ")
            dob=raw_input("enter the dob : ")
            age=raw_input("enter the age : ")
            mark=[]
            for item in range(0,5):
                x=input("enter the marks :")
                mark.append(x)
                print max
        
            std1=Student(rollno, name, dob, age, mark)
            std1.displayStudent()
            print"the sum is : ",std1.add()
            print"the avg is : ",std1.avg()
            std1.calculategrade()
            std1.scholarship()
            
