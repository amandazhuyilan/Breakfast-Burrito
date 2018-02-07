# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.


class Solution:
    def deduplication(self, nums):
        if len(nums) < 1 or nums is None:
            return 0
        # write your code here
        nums = sorted(nums)
        index = 0
        for i in range(len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
        return index+1


print(Solution().deduplication([1, 2, 3, 2, 3, 4, 4]))
