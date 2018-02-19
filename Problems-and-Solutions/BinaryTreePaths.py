class Solution:
    """
    @param: root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        # write your code here
        result = []
        if root is None:
            return result
        self.dfs(root, result, [])
        return result

    def dfs(self, node, result, temp):
        temp.append(str(node.value))
        if node.left is None and node.right is None:
            result.append("->".join(temp))
            temp.pop()

        if node.left:
            self.dfs(node.left, result, temp)
        if node.right:
            self.dfs(node.right, result, temp)
        temp.pop()



input_tree={1,2,3,4,5}
print(Solution().binaryTreePaths(input_tree))