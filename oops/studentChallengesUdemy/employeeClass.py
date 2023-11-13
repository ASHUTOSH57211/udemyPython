#Question create a class employee with instance variable and class variable with class methods

class Employee:
    employee_count = 100 
    

    def __init__(self,name,salary,designation):
        self.name = name
        self.salary = salary
        self.designation = designation
        self.e_id = "e"+ str(Employee.employee_count)
        Employee.employee_count += 1

    def show_details(self):
        print(self.e_id)
        print(self.name)
        print(self.salary)
        print(self.designation)
    
    @classmethod
    def total_countmployees(cls):
        return cls.employee_count-100

emp1 = Employee("Ashu",10000,"SE")
emp2 = Employee("Rambo",12000,"ASE")  

emp1.show_details()
emp2.show_details()

print(Employee.total_countmployees())