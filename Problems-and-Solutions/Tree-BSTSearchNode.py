def searchNode(node, val):
    if node is None:
        return False
    if node.value == val:
        return True
    if node.value > val:
        return searchNode(node.left, val)
    if node.value < val:
        return searchNode(node.right, val)
    