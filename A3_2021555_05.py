class Student:
    def __init__(self,name,cgpa,branch):
        self.name=name
        self.cgpa=cgpa
        self.branch=branch
        self.isPlaced=False
    
    def isEligible(self,com):
        if self.cgpa>=com.requiredcgpa() and self.branch in com.lstofbranches() and self.isPlaced==False:
            print(f'Student {self.name} is eligible for company {com.companyname()}')
            return True
        else:
            print(f"Student {self.name} is not eligible for company {com.companyname()}")
    
    def apply(self,com):
        if stu.isEligible(com)==True:
            com.appliedStudents.append(self.name)
    
    def getsPlaced(self):
        self.isPlaced=True
    
class Company(Student):
    def __init__(self,compname,reqcgpa,branches,posOpen):
        self.compname=compname
        self.reqcgpa=reqcgpa
        self.branches=branches
        self.posOpen=posOpen
        self.appliedStudents=[]
        self.applicationOpen=True
    
    def requiredcgpa(self):
        return self.reqcgpa
    
    def lstofbranches(self):
        return self.branches
    
    def hireStudents(self):
        if self.applicationOpen==True:
            for i in range(0,self.posOpen):
                print(i)                                    # counter + check
                print(self.appliedStudents[i])
                
        stu.getsPlaced()
        self.closeApplication()
    
    def closeApplication(self):
        self.applicationOpen=False
        print(len(self.appliedStudents))
    
    def companyname(self):
        return self.compname



t=tuple()
n=int(input("No. of students:"))
for i in range(0,n):
    name=input("Name of student:")
    cgpa=float(input("Enter cgpa:"))
    branch=input("Enter branch:")
    stu=Student(name,cgpa,branch)
    t=t+(stu,)

k=int(input("Enter no. of companies:"))
    

for i in range(k):
    compname=input("Enter company name:")
    reqcgpa=float(input("Enter required cgpa:"))
    reqbranches=[x for x in input("Enter appropriate branches:").split()]
    posOpen=int(input("Enter number of positions that are open:"))
    com=Company(compname,reqcgpa,reqbranches,posOpen)
    for i in t:    
        i.apply(com)
    
    com.hireStudents()



    
    












        
        
    