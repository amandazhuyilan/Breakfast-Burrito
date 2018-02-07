class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if target not in nums:
            return -1
        index = self.BinarySearch(0, len(nums) - 1, nums, target)

        if index < len(nums) - 1:         
            if nums[index] == target and nums[index + 1] != target:
                return index
            else:
                while nums[index] == target and nums[index + 1] == target and index < len(nums) - 1:
                    return index + 1
        return index 
        
    def BinarySearch(self, startIndex, endIndex, nums, target):
        while startIndex + 1 < endIndex:
            mid = (startIndex + endIndex)//2
            if nums[mid] == target:
                return mid 
            if nums[mid] < target:
                return self.BinarySearch(mid + 1, endIndex, nums, target)
            if nums[mid] > target:
                return self.BinarySearch(startIndex, mid - 1, nums, target)  
        return startIndex
        
    
input_list = [1,2,2,4,5,5]
print(Solution().lastPosition(input_list,5))