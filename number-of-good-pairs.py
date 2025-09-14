class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        goodPairs=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
             if nums [i]==nums[j]:
                goodPairs+=1
        return goodPairs
        