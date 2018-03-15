class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n is None:
            return None
        result = []
        result_int = []
        for p in self.partition(n):
            result_int.append(p)

        for k in result_int:
            result_temp = []
            print(k)
            for j in k:
                result_temp.append(self.genPairs(j))
            result.append(''.join(result_temp))
        return result

    def genPairs(self,n):
        result = []
        for i in range(n):
            result.append('(')
        for j in range(n):
            result.append(')')
        return ''.join(result)

    def partition(self, n):
        if n == 0:
            yield []
            return

        for p in self.partition(n-1):
            yield [1] + p
            if p and (len(p) < 2 or p[1] > p[0]):
                yield [p[0] + 1] + p[1:]

s = Solution()
print(s.generateParenthesis(4))
