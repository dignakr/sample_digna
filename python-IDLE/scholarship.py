from datetime import date
class Student:
    
    def __init__(self, name, date1, duration, amount):
        
        self.name=name
        self.date1=date1
        self.duration=duration
        self.amount=amount
        

    def displayStudent(self):
        print "Name : ",self.name
        print "Date : ", self.date1
        print "Duration : ", self.duration
        print "Amount : ", self.amount

    def checkExpiry(self,dat1,duration):
         
         dat=date.today()
         
         diff=abs((dat - dat1).days)
         print diff
         if(diff > duration):
             print"Sorry scholarship date is expired"
         else:
             print"Not Expired"
             

if __name__ == "__main__":

      print "Enter the number of students : "
      limit = input()
      for i in range(0,limit):      
            name=raw_input("enter the name : ")
            date1=raw_input("enter the date of scholarship: ")
            ls=map(int,date1.split("-"))
            dat1=date(ls[0],ls[1],ls[2])
            
            duration=input("enter the duration : ")
            amount=raw_input("enter the amount : ")
            std1=Student(name, date1,duration, amount)
            
            std1.displayStudent()
            std1.checkExpiry(dat1,duration)
