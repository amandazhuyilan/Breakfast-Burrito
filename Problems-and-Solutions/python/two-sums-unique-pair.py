class Solution:
    """
    @param: nums: an array of integer
    @param: target: An integer
    @return: An integer
    """
    def twoSum_unique_pairs(self, nums, target):
        # write your code here
        if nums == [] or len(nums) < 2:
            return 0
        nums = sorted(nums)
        count = 0
        start = 0
        end = len(nums) -1 
        while (start < end):
            if (nums[start] + nums[end] == target):
                count += 1
                start += 1 
                end -= 1
                while (start < end and nums[start] == nums[start -1]):
                    start += 1
                while(start < end and nums[end] == nums[end + 1]):
                    end -=1
            elif (nums[start] + nums[end] > target):
                end -= 1
            elif (nums[start] + nums[end] < target):
                start += 1
        return count
                
nums = [7,11,11,1,2,3,4]
target = 22
print(Solution().twoSum_unique_pairs(nums, target))