from neetcode.arrays_and_hashing.valid_anagram import solution
from neetcode.arrays_and_hashing.valid_anagram.solution import Solution

def test_valid_anagram():
    solution = Solution()
    assert solution.isAnagram("anagram", "nagaram")
    assert not solution.isAnagram("rat", "car")
    assert solution.isAnagram("a", "a")
    assert not solution.isAnagram("a", "b")

# TODO: Add more test cases
