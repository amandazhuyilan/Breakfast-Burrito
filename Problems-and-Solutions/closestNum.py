class Solution:
    """
    @param: A: an integer array sorted in ascending order
    @param: target: An integer
    @return: an integer
    """
    def closestNumber(self, A, target):
        # write your code here
            if len(A) == None:
                return -1

            if target - 1 > A[-1] or target + 1 < A[0]:
                return -1

            result = self.BinarySearch(0,len(A), A, target)
            return result
    
    def BinarySearch(self,startIndex, endIndex, A, target):
        if startIndex > endIndex:
            return -1
            
        mid = (startIndex + endIndex)//2
        if target == A[mid]:
            return mid
        
        if target + 1 == A[mid] or target - 1 == A[mid]:
            return mid
            
        if target + 1 > A[mid]:
            return self.BinarySearch(mid, endIndex, A, target)

        if target - 1 < A[mid]:
            return self.BinarySearch(startIndex, mid, A, target)
            

print(Solution().closestNumber([1,4,6,10,20],21))