class Solution:
	def BinarySearch(self, startIndex, endIndex, nums, target):
		if len(nums) == 0:
			return -1
		startIndex, endIndex = 0, len(nums)+1

		nums = sorted(nums)

		while startIndex + 1 < endIndex:
			mid = (startIndex + endIndex)//2
			if nums[mid] == target:
				return mid 
			if nums[mid] < target:
				self.BinarySearch(mid + 1, endIndex, nums, target)
			if nums[mid] > target:
				self.BinarySearch(startIndex, mid - 1, nums,target)
			return -1

Solution().BinarySearch(0,4,[1,4,3,7,8], 3)