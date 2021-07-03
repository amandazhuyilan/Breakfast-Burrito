class Solution:
	def CombinationSum(self, nums, target):
		result = []
		self.dfs(sorted(nums), target, 0, [], result)
		return result 

	def dfs(self, nums, target, startIndex, temp, result):
		if target < 0:
			return 
		if target == 0:
			result.append(temp)
		for i in range(startIndex, len(nums)):
			self.dfs(nums, target-nums[i], i, temp+[nums[i]], result)


test_nums = [2,3,4,5,6,7]
test_target = 7
print(Solution().CombinationSum(test_nums, test_target))