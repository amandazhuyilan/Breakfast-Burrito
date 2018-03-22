# Generating an int as a sum of zero or more positive ints
def partition(n):
    if n == 0:
        yield []
        return 

    for p in partition(n - 1):
        print("print 1: " ,([1] + p))
        yield [1] + p
        print("Got here")
        print("n: ", n)
        if p and (len(p) < 2 or p[1] > p[0]):
            print("p in 2: ", p)
            print("print2: " ,[p[0] + 1] + p[1:])
            yield [p[0] + 1] + p[1:] 

for i in partition(4):
    print(i)

