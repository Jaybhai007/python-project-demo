class Employee:
    def __init__(self,emp_id,name,deparment,salary):
        self.emp_id = emp_id
        self.name = name
        self.department = deparment
        self.salary = salary

    def to_dict(self):
        return{
            "Emp_id" : self.emp_id,
             "name" : self.name,
             "department" : self.department,
             "salary" : self.salary
        }

