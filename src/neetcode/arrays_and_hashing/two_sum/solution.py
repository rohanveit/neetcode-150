class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = dict()
        for idx, item in enumerate(nums):
            complement = target - item
            if complement in seen.keys():
                return sorted([idx, seen[complement]])
            seen[item] = idx

        return []
        
        
        