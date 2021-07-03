
class Solution:
    def permutation(self, nums):
        result = []
        self.permute(nums, 0, result)
        return result

    def permute(self, nums, startIndex, result):
        if startIndex == len(nums):
            result.append([] + nums)
        else:
            for i in range(startIndex, len(nums)):
                nums[startIndex], nums[i] = nums[i], nums[startIndex]
                self.permute(nums, startIndex + 1, result)
                nums[startIndex], nums[i] = nums[i], nums[startIndex]  # backtrack


    def permutation_string(self, s):
        s = list(s)

        result = []
        self.permutation_string_recur(s, 0, result)
        return result

    def permutation_string_recur(self, s, startIndex, result):
        if startIndex == len(s):
            print([] + s)
            result.append([] + s)
        else:
            for i in range(startIndex, len(s)):
                s[i], s[startIndex] = s[startIndex], s[i]
                self.permutation_string_recur(s, startIndex + 1, result)
                s[i], s[startIndex] = s[startIndex], s[i]
# # Driver program to test the above function
nums = [1,2,3]
s = "abc"
print(Solution.permutation(Solution(),nums))
print(Solution.permutation_string(Solution(), s))
