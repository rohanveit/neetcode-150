from neetcode.arrays_and_hashing.two_sum import solution
from neetcode.arrays_and_hashing.two_sum.solution import Solution

def test_two_sum():
    solution = Solution()

    print(solution.twoSum([2, 7, 11, 15], 9))
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]
    assert solution.twoSum([1, 2, 3, 4, 5], 10) == []
    assert solution.twoSum([], 5) == []