class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return False
        temp = []
        s = list(s)
        # if '(' not in s and'{' not in s  and '[' not in s:
        #     return False
        
        for i in s:
            if i == '(' or i == '[' or i == '{':
                temp.append(i)
                # continue
            if i == ')':
                if len(temp) > 0 and temp[-1] == '(':
                    temp = temp[:-1]
                else:
                    return False
            if i == ']':
                if len(temp) > 0 and temp[-1] == '[':
                    temp = temp[:-1]
                else:
                    return False
            if i == '}':
                if len(temp) > 0 and temp[-1] == '{':
                    temp = temp[:-1]
                else:
                    return False

        if len(temp) == 0:
            return True
        return False
