class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.minStack = []
        self.minValue = []
    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        if number is None:
            return None
        if len(self.minValue) == 0 or number <= self.minValue[-1]:
            self.minValue.append(number)
        self.minStack.append(number)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if self.minStack[-1] == self.minValue[-1]:
            self.minValue.pop()

        return self.minStack.pop()
        
    """
    @return: An integer
    """
    def min(self):
        # write your code here
        if len(self.minStack) == 0:
            return None
        return self.minValue[-1]


stack = MinStack()
stack.push(5)
stack.push(5)
stack.push(4)
stack.push(4)
stack.min()
stack.pop()
stack.pop()
stack.push(3)
stack.min()
stack.push(3)
stack.min()
stack.pop()
stack.push(2)
stack.push(2)
stack.push(1)
stack.push(1)
stack.min()
stack.pop()
stack.pop()