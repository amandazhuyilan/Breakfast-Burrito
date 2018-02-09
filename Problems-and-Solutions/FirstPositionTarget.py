class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        start = 0 
        end = len(nums) - 1
        if nums is None or len(nums) == 0:
            return -1
        if target > nums[-1] or target < nums[0]:
            return -1
            
        while start + 1 < end:
            mid = (start + end)//2
            if nums[mid] == target:
                while nums[mid] == target:
                    mid -= 1
                return mid + 1
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1

        if nums[start] == target:
            return start
        elif nums[end] == target:
            while nums[end] == target:
                end -= 1
            return end + 1
        else:
            return -1
                
print(Solution().binarySearch([2,2,3,4,5,6,8,13,17,18],17))