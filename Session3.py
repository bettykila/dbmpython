#string
a = "Apple"
#List
course = ["CCIT", "CCDM"]
#Tuple
tupledemo = (2004202332, "Betty Kila")

print (type(a)) #output: <class 'str'>

print (type(course)) #output: <class 'list'>

print (type(tupledemo)) #output: <class 'tuple'>

#dictionary
#create a dictionary and call this staff
#it should contain details: 
#ID: 1102, Name: Shirley Komogi, Role: IT Trainer, Phone: 3267424

Staff = {"ID": 1102, "Name": "Shirley Komogi", "Role": "IT Trainer", "Phone": 3267424}

print (Staff)

#Access the role of this staff by using key
print (Staff ['Role'] ) #output: IT Trainer

#Exercise 1
#Q1. Create an object to hold this data. Call it CEITcourses (DICTIONARY)
CEITcourses = {1001: "CCLSA", 1002: "CCIT", 1003: "CCDM", 1004: "CCNS"}
print (CEITcourses)
# output: {1001: 'CCLSA', 1002: 'CCIT', 1003: 'CCDM', 1004: 'CCNS'}

#Q2. Create another object to hold all realated permanent data for schools in UPNG. Call it UPNGschools (TUPLE)
UPNGschools = (["SOL", 120], ["SHSS", 90], ["SMHS", 150], ["SNPS", 100], ["SBPP", 200])
print(UPNGschools)
# output: (['SOL', 120], ['SHSS', 90], ['SMHS', 150], ['SNPS', 100], ['SBPP', 200])

#Q3. Create an object to hold this temporary data for staff. This should contain only the ID, Name and role. 
#Call these objects StaffJT, StaffJM
StaffJT = [223, "John Tambu", "Payroll Officer"]
StaffJM = [332, "Jimmy Masin", "Auditor"]
print(StaffJT) # output: [223, 'John Tambu', 'Payroll Officer']
print(StaffJM) # output: [332, 'Jimmy Masin', 'Auditor']

#Q3.1 Jimmy got a promotion to be the Senior Auditor. Update his role. 
StaffJM[2] = "Senior Auditor"
print (StaffJM)
# output: [332, 'Jimmy Masin', 'Senior Auditor']

#Q3.2 use the type function to confirm that the objects you created are the correct type.

print (type(CEITcourses)) # output: <class 'dict'>
print (type(UPNGschools)) # output: <class 'tuple'>
print (type(StaffJM)) #output: <class 'list'>
print(type(StaffJT)) #output: <class 'list'>
