def summ(list1):    
    s=float(sum(list1))
    return s

def avg(list1):
    av=summ(list1)/len(list1)
    return av
    
if __name__ == "__main__":        
        x=raw_input("enter the list elements : ")
        list1 =map(int ,x.split(","))
        print"the list is : ",list1
        print"the sum is : ",summ(list1)
        print"the avg is : ",avg(list1)
