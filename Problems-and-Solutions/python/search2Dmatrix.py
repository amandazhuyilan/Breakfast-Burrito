class Solution:
  def searchMatrix(self, matrix, target):
      if len(matrix) == 0 or target == None:
          return 0
      endIndex = len(matrix[0]) - 1
      counter = 0

      for i in range(len(matrix)):
          res = self.BinarySearch(matrix, 0, endIndex, i, target)
          if res == True:
              counter += 1
      return counter

  def BinarySearch(self, matrix, startIndex, endIndex, rowNum, target):
    while startIndex <= endIndex:
        mid = (startIndex + endIndex)//2

        if matrix[rowNum][mid] == target:
            return True

        if matrix[rowNum][mid] < target:
            return self.BinarySearch(matrix, mid + 1, endIndex, rowNum, target)

        elif matrix[rowNum][mid] > target:
            return self.BinarySearch(matrix, startIndex, mid - 1, rowNum, target)

    return False


# class Solution:
#     # @param {integer[][]} matrix
#     # @param {integer} target
#     # @return {boolean}
#     def searchMatrix(self, matrix, target):
#         counter = 0
#         y = len(matrix[0]) - 1

#         def binSearch(nums, low, high):
#             while low <= high:
#                 mid = (low + high) // 2
#                 if nums[mid] > target:
#                     high = mid - 1
#                 else:
#                     low = mid + 1
#             return high
#         for x in range(len(matrix)):
#             y = binSearch(matrix[x], 0, y)
#             if matrix[x][y] == target:
#                 counter += 1
#         return counter


matrix = [
    [1, 3, 5, 7],
    [2, 4, 7, 8],
    [3, 5, 9, 10]
]

print(Solution().searchMatrix(matrix, 3))
