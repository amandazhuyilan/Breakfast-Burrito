# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

class Solution:
    """
    @param: nums: an integer array
    @return: 
    """
    def moveZeroes(self, nums):
        # write your code here
        result = [0] * len(nums)
        i = 0
        for index, number in enumerate(nums):
            if number != 0:
                result[i] = number
                i += 1
        return result

print(Solution().moveZeroes([1,0,0,0,3,12]))