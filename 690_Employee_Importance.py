class Employee():
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self,employees,id):
        emp_hash = {}
        for employee in employees:
            emp_hash[employee.id] = employee
        
        def iter(employees,emp_hash,id):
            temp = 0
            for subid in emp_hash[id].subordinates:
                temp += iter(employees,emp_hash,subid)
            return temp + emp_hash[id].importance
        return iter(employees,emp_hash,id)
