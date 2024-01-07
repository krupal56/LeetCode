class Solution:
    def average(self, salary: List[int]) -> float:
        low = min(salary)
        high = max(salary)
        if len(salary) == 3:
            salary.sort()
            return salary[1]
        if len(salary) < 3:
            return ('Error')
        else:
            salary.sort()
            salary_new = salary[1:-1]
            return sum(salary_new)/len(salary_new)