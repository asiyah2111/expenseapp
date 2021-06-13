from models import Category, Expense

class Service:
    catList = []
    expList = []
    
    def startApp(self):
        while True:
            choice = self.printOptions()
            if choice == 1:
                self.addCategory()
            elif choice == 2:
                self.catListing()
            elif choice == 3:
                self.expenseEntry()
            elif choice == 4:
                self.reportCatWise()
            elif choice == 5:
                self.reportMonthWise()
            elif choice==6:
                self.reportMonthRange()
            elif choice==7:
                self.reportAmountRange()
            elif choice == 8:
                break
    
    def printOptions(self):
        print("1. Add Category")
        print("2. Category Listing")
        print("3. Expense Entry")
        print("4. Report Category Wise")
        print("5. Report Month Year")
        print("6. Report Month range")
        print("7. Report Amount Range")
        print("8. Exit")
        ch = int(input("Enter choice: "))
        return ch

    def addCategory(self):
        try:
            catid = int(input("Enter Category ID: "))
        
            
            cname = input("Enter Category Name: ")
            cid=[]
            nm=[]
            for i in Service.catList:
                cid.append(i.getCatId())
                nm.append(i.getCatName())
                
            
            #Check for duplicate Cat ID.
            if catid in cid or cname in nm:
                print("already exist")
            else:
                c=Category()
                c.setCatId(catid)
                c.setCatName(cname)
                Service.catList.append(c)
                
                print("done")
        except:
            print('id should be a number.....!!!!')

           
    def catListing(self):
        j = 1
        for i in Service.catList:
            print(j, i.getCatId(), i.getCatName())
            j = j + 1

    def expenseEntry(self):
        self.catListing()
        catid = int(input("Select Category to add expenses: "))

        amount = float(input("Enter Amount: "))
        remark = input("Enter Remark: ")
        date = input("Enter Date (dd/mm/yyyy): ")

        
        e = Expense()
        e.setAmount(amount)
        e.setRemark(remark)
        e.setDate(date)
        e.setCategoryId(catid)

        Service.expList.append(e)
        print("Expenses Added!")

    def reportCatWise(self):
        self.catListing()
        catid = int(input("Select Category to add expenses: "))

        for i in Service.expList:
            if i.getCategoryId() == catid:
                print(i.getAmount(), i.getRemark(), i.getDate())
                
    def reportMonthWise(self):
        y = int(input("Enter Year: "))
        m = int(input("Enter Month (01-12): "))

        for i in Service.expList:
            dt = i.getDate() #'dd/mm/yyyy'
            newdt = dt.split("/") #['dd', 'mm', 'yyyy']
            if y == int(newdt[2]) and m == int(newdt[1]):
                print(i.getAmount(), i.getRemark(), i.getDate())

    def reportMonthRange(self):
        y= int(input("Enter year: "))
        m1= int(input("Enter starting month: "))
        m2= int(input("enter last month: "))
        for i in Service.expList:
            dt = i.getDate()
            newdt = dt.split("/")
            if y== int(newdt[2]) and int(newdt[1]) in range(m1,m2):
                print(i.getAmount(), i.getRemark(), i.getDate())


    def reportAmountRange(self):
        a1=float(input("enter starting amount: "))
        a2=float(input("enter ending amount: "))
        for i in Service.expList:
            am= i.getAmount()
            if am in range(a1,a2):
                print(i.getAmount(), i.getRemark(), i.getDate())

                
            
                

"""
Task1: Report Month Range: Year, m1, m2.
Task2: Report Amount range: a1, a2 (500, 1000)
Task3: Exception handling
Task4: Stores only unique Cat ID.
"""

        


obj = Service()
obj.startApp()
