from neetcode.arrays_and_hashing.top_k_list_elements.solution import Solution

def test_top_k_frequent():
    sol = Solution()
    assert sol.topKFrequent([1,1,1,2,2,3], 2) == [1,2]
    assert sol.topKFrequent([1], 1) == [1]