 class Solution(object):
    def numIdenticalPairs(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and i<j:
                    n+=1
        return n      
