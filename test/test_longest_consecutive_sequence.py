from neetcode.arrays_and_hashing.longest_consecutive_sequence.solution import Solution

def test_longest_consecutive_sequence():
    sol = Solution()

    assert sol.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
    assert sol.longestConsecutive([]) == 0
    assert sol.longestConsecutive([1,2,0,1]) == 3
    assert sol.longestConsecutive([9,1,-3,2,4,8,3,-1,6,-2,-4,7, 10]) == 5
