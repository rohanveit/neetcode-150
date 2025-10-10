from neetcode.arrays_and_hashing.array_product_except_self.solution import Solution

def test_array_product_except_self():
    solution = Solution()
    nums = [1,2,3,4]
    assert solution.productExceptSelf(nums) == [24,12,8,6]
