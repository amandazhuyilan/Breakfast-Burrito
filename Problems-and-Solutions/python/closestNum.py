class Solution:
    def closestNum(self, A, target):
        if len(A) == 0 or target == None:
            return -1
        startIndex = 0
        endIndex = len(A) - 1

        while(startIndex + 1 < endIndex):
            mid = (startIndex + endIndex)//2

            if target == A[mid]:
                return mid
            elif target < A[mid]:
                endIndex = mid
            elif target > A[mid]:
                startIndex = mid

        if abs(target-A[startIndex]) < abs(target-A[endIndex]):
            return startIndex
        else:
            return endIndex

print(Solution().closestNum([1,3,4,8],6)) 