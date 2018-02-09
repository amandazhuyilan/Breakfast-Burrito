# Find any position of a target number in a sorted array. Return -1 if target does not exist.

class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        start = 0
        end = len(nums) - 1

        if len(nums) == 0 or nums is None:
            return -1
            
        if target > nums[-1] or target < nums[0]:
            return -1
        
        while start + 1 < end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
        
        if nums[-1] == target:
            return len(nums)-1
        elif nums[0] == target:
            return 0
        else:
            return -1
      