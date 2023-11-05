class person:
    def person_info(self,name,age):
        print("inside person class")
        print("name:", name, "age:", age)

class Company:
    def company_info(self, company_name, location):
        print("inside company class")
        print("name:", company_name, "location:", location)

class Employee(person, Company):
    def Employee_info(self,salary,skill):
        print("inside employee class")
        print("salary:", salary, "skill:", skill)

emp = Employee()

emp.person_info("jessa",28)
emp.company_info("google","atlanta")
emp.Employee_info(12000,"machine learning")

