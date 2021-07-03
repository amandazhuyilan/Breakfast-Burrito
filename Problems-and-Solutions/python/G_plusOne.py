# Leetcode 66 plus one
# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

# You may assume the integer do not contain any leading zero, except the number 0 itself.

# The digits are stored such that the most significant digit is at the head of the list.

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits is None:
        	return None

        temp = 0
        result = []
        s_len = len(digits) - 1
        for i in range(len(digits)):
        	temp = temp + digits[i] * 10 ** (s_len)
        	s_len = s_len - 1

        temp = temp + 1
        temp_str = str(temp)

        l = len(temp_str) - 1
        for j in range(len(temp_str)):
        	result.append(temp // (10 ** l))
        	temp = temp % (10 ** l) 
        	l = l - 1

        return result



s = Solution()
print(s.plusOne([9,9,9]))
