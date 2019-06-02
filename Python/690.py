"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
# 递归求解
class Solution:
    def getImportance(self, employees: 'list<Employee>', id: 'int') -> 'int':
        score = 0
        for v in employees:
            if v.id == id:
                score += v.importance
                for val in v.subordinates:
                    # 递归求解每个下属的重要性
                    score += self.getImportance(employees, val)
                break
        return score

