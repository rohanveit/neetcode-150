from neetcode.arrays_and_hashing.encoding_decoding_strings.solution import Solution

def test_encode_decode_strs():
    input = ["hello", "world"]
    solution = Solution()
    encoded = solution.encode_strs(input)
    
    assert solution.decode_strs(encoded) == input

def test_empty_list():
    input = []
    solution = Solution()
    encoded = solution.encode_strs(input)
    
    assert solution.decode_strs(encoded) == input