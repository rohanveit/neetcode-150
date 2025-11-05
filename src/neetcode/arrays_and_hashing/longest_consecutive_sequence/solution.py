class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        longest_streak = 0
        current_streak = 0
        previous_num = None
        for num in nums:

            if previous_num is None:
                current_streak += 1
            elif num == previous_num + 1:
                current_streak += 1
            elif num == previous_num:
                current_streak += 0
            else:
                current_streak = 1
            previous_num = num
            longest_streak = max(longest_streak, current_streak)
            # print(f'\nnew num: {num}\n\nnew streak:{current_streak}\nlongest:{longest_streak}')


        return longest_streak
