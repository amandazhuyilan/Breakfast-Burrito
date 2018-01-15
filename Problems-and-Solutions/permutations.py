
class Solution:
    def permutation(self,nums):
        result = []
        self.permute(nums, 0, result)
        return result

    def permute(self,nums, startIndex,result):
        if startIndex==len(nums):
            result.append([] + nums)
        else:
            for i in range(startIndex,len(nums)):
                nums[startIndex], nums[i] = nums[i], nums[startIndex]
                self.permute(nums, startIndex + 1, result)
                nums[startIndex], nums[i] = nums[i], nums[startIndex] # backtrack

     
# # Driver program to test the above function
nums = [1,2,3]
print(Solution.permutation(Solution(),nums))
#print(permutation([1,2,3]))

