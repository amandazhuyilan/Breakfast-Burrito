# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place, do not allocate extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


class Solution:
    def nextPermutation_itertools(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # solved by using itertools module
        import itertools

        result = list(itertools.permutations(nums, len(nums)))
        if result.index(tuple(nums)) == len(result) - 1:
            nums = list(result[0])
        else:
            nums = list(result[result.index(tuple(nums)) + 1])

    def lexicographically_next_permutation(self, nums):
    	# find first lasrgest number from the back
        i = len(nums) - 2
        while not (i < 0 or nums[i] < nums[i + 1]):
            i -= 1
       	if i < 0:
        	nums = nums[::-1]
        	return nums

        j = len(nums) - 1
        # find second largest number from the back
        while not (nums[j] > nums[i]):
            j -= 1
        # swap
        nums[i], nums[j] = nums[j], nums[i]
        # reverse
        nums[i + 1:] = reversed(nums[i + 1:])
        return nums


s = Solution()
# print(s.nextPermutation_itertools([1, 2, 3]))
print(s.nextPermutation_itertools([1, 4, 2, 5, 3]))
print(s.lexicographically_next_permutation([3,2,1]))
