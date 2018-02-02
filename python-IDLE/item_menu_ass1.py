class ItemList:
        def __init__(self, itemname, itemcode):
            self.itemname = itemname
            self.itemcode = itemcode
           
        def display(self):
            
            print '[itemname :',self.itemname,',itemcode :',self.itemcode,']' 

                
            
if __name__=="__main__":
    ans=True
    l=list()
    
    while ans:
            print ("""
                1.Add items
                2.Display items
                3.Delete Items
                4.View Items
                5.Exit/Quit           
                """)
            ans=raw_input("What would you like to do? ")
            
            if ans=="1":              
                 itemname=raw_input("Enter item name: ")
                 itemcode = raw_input("Enter item code: ")
                 item1=ItemList(itemname,itemcode)
                 l.append(item1)
                
                 
            elif ans=="3":
                  c=raw_input("which item to delete? ")
                  for i in l:
                        if i.itemname==c:
                            k=l.index(i)
                            l.remove(i)
                            print'The item is deleted successfully'

            elif ans=="2":
                for item in l:
                    item.display()
            elif ans=="4":
                itm=raw_input('Enter an item you want to be displayed :')
                for i in l:
                    if i.itemname==itm:
                        k=l.index(i)
                        print 'The index of the item is :',k
                        temp=l[k]
                        print 'The Item details are :[itemname :',temp.itemname,',itemcode :',temp.itemcode,']'
            elif ans=="5":
                print("\n bye") 
                exit()
       
            else:
              print("\n Not Valid Choice Try again") 
