# Letter Combinations of a Phone Number
# Given a digit string, return all possible letter combinations that the number could represent. A mapping of digit to letters is just like on the telephone buttons.


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digits = list(digits)
        result = []
        look_up_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        for i in digits:
            if i in look_up_dict and len(result) == 0:
                result = look_up_dict.get(i)
                continue

            if i in look_up_dict and len(result) > 0:
                temp = []
                for j in result:
                    for k in look_up_dict.get(i):
                        temp.append(j + k)
                if temp is not None:
                    for m in temp:
                        result.append(m)
        result = list(filter(lambda x: len(x) == len(digits), result))
        # remove duplicate
        final_result = []
        for element in result:
            if element not in final_result:
                final_result.append(element)
        return final_result
s = Solution()
print(s.letterCombinations("234"))
            
