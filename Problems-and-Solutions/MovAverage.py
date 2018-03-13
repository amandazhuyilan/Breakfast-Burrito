class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        if size is None or size == 0:
            self.num_list = None
            
        self.num_list = []
        self.size = size
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.num_list) == 0 and val is not None:
            self.num_list.append(val)
            return val
        
        if val is None:
            return float((sum(self.num_list[-3:]))/len(self.num_list))
        
        elif len(self.num_list) < self.size:
            self.num_list.append(val)
            return float(sum(self.num_list)/len(self.num_list))
        else:
            print('haha')
            self.num_list.append(val)
            return float(sum(self.num_list[-self.size:])/ self.size)

obj = MovingAverage(3)
print(obj.next(1))

print(obj.next(10))

print(obj.next(3))

print(obj.next(5))
print(obj.num_list[-3:])