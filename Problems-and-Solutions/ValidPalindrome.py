# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

class Solution:
    def isPalindrome(self, s):
        string_input = []
        s = s.lower()
        for i in s:
            if i.isalpha() or i.isdigit():
                string_input.append(i)
        string_list = list(string_input)

        if string_list is None:
            return False

        start = 0
        end = len(string_list) - 1

        while(start < end):
            if string_list[start] != string_list[end]:
                return False
            else:
                start += 1
                end -= 1
        return True


print(Solution().isPalindrome("1a2"))
