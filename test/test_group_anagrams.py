from neetcode.arrays_and_hashing.group_anagram.solution import Solution

def test_group_anagrams():
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected_output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    solution = Solution()
    output = solution.groupAnagrams(input)
    
    
    # Sort inner lists for comparison
    output = [sorted(group) for group in output]
    expected_output = [sorted(group) for group in expected_output]
    
    # Sort outer list for comparison
    output.sort()
    expected_output.sort()
    
    assert output == expected_output