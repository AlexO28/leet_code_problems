# You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.
# You are given an array of employees employees where:
# Given an integer id that represents an employee's ID, return the total importance value of this employee and all their direct and indirect subordinates.
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.employee_dict = {employee.id: employee for employee in employees}
        return self.calculate_importance(id)

    def calculate_importance(self, id: int) -> int:
            employee = self.employee_dict[id]
            total_importance = employee.importance
            for subordinate_id in employee.subordinates:
                total_importance += self.calculate_importance(subordinate_id)
            return total_importance
