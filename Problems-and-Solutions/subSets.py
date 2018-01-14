# Lintcode 17. Given a set of distinct integers, return all possible subsets.
# Example
# If S = [1,2,3], a solution is:

# [ [3], [1], [2], [1,2,3], [1,3], [2,3], [1,2],[]]


def subsets(nums):
    results = []
    subset = []

    if nums is None or len(nums) == 0:
        return results
    
    nums.sort()

    DFS(0, nums, subset, results)
    
    return results
    

def DFS(startIndex, nums, subset, results):
    results.append([] + subset)
    print(results)

    for i in range(startIndex, len(nums)):            
        subset.append(nums[i])
        DFS(i + 1, nums, subset, results)
        # remove the last element in the seubset
        subset.pop()


nums = [2, 1, 3]
print(subsets([2,1,3]))
          





