# For a given list of ints a, return the number of unique pairs that sums up to the target
# a is the number list and k is the target
def numberOfPairs(a, k):
    #
    # Write your code here.
    #
    if a is None or k is None:
        return None
    
    a.sort()
    print(a)
    start = 0
    last_i = a[0] - 1
    result = []
    
    while (start < len(a) - 1):
        end = len(a) - 1
        if last_i == a[start]:
            start += 1
            continue

        last_i = a[start]
            
        while (start < end):
            if a[start] + a[end] > k:
                end -= 1
            elif a[start] + a[end] < k:
                last_i = a[start]
                start += 1
                break
            elif a[start] + a[end] == k:
                print(a[start], a[end])
                result.append((a[start], a[end]))
                last_i = a[start]
                start += 1
                break
        
    return result

print(numberOfPairs([6,1,3,46,1,3,9],47))
# print(numberOfPairs([7,6,6,3,9,3,5,1],12))
