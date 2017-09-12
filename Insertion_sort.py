#Solution 1: Brutal force. O(n^2)
class Solution_BrutalForce:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        
        for i in range (len(nums)):
            for j in range (1,len(nums)-i):
                if nums[i] + nums[i+j] == target:
                    return [i, i+j]
                
#Solution 2: Use dictionary. buffer_dictionary[target-nums[i]] = i if nums[i] not in buffer dictionary.               
class Solution_Dictionary(object):
    def twoSum(self, nums, target):
        if len(nums) <=1:
            return False
        buff_dic = {}
        for i in range(len(nums)):
            if nums[i] in buff_dic:
                return [buff_dic[nums[i]], i]
            else: 
                buff_dic[target-nums[i]] = i
