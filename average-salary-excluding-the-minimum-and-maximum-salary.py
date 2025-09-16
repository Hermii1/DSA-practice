class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        min_salary = min(salary)
        max_salary = max(salary)
        total_sum = sum(salary)
        adjusted_sum = total_sum - min_salary - max_salary
        count = len(salary) - 2
        return adjusted_sum / float(count)