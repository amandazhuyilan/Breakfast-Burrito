# Given an array of n integer, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.

class Solution:
    """
    @param: nums: a list of integers.
    @param: k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        # ends at index n - k 
        if k <= 0 or k > len(nums):
            return []
        n = len(nums)
        sums = [0] * (n - k + 1)
        for i in range(k):
            sums[0] += nums[i]
        
        for i in range(1, n - k + 1):
            sums[i] = sums[i-1] - nums[i - 1] + nums[i + k - 1]
            
        return sums

print(Solution().winSum([1,2,7,8,5],1))