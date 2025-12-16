class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        # Method:1-> O(N2)
        # for i in range(0,n+1):
        #     if i not in nums:
        #         return i
        # return None
        expected_sum = n *(n+1)//2
        actual_s = sum(nums)
        return expected_sum-actual_s
        