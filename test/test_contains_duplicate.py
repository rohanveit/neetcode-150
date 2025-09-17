from neetcode.arrays_and_hashing.contains_duplicate.solution import Solution

def test_contains_duplicate():
    solution = Solution()
    assert solution.containsDuplicate([1, 2, 3, 1])
    assert not solution.containsDuplicate([1, 2, 3, 4])
    assert solution.containsDuplicate([1, 1, 1, 1])
    assert not solution.containsDuplicate([])

# TODO: Add more test cases