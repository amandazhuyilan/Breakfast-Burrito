# Given a non-negative number represented as an array of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.

# Solution: Transform input int array into an actual number, plus one, determine if there is a carry operation where the length increased by one, then append the numbers into the result list.


"""
@param: digits: a number represented as an array of digits
@return: the result
"""
def plusOne(digits):
    # write your code here
    num_val = 0
    result = []
    if len(digits) < 1:
        print("digit not present!\n")
        
    for i, num in enumerate(digits):
        num_val = num_val + num*10**(len(digits)-i-1)
    
    num_val = num_val + 1
    
    if 0<= num_val//(10**(len(digits)-1)) <= 9:
    # The input number remains the same length
        if len(digits)<2 and num_val != 10:
            result.append(num_val)
        else:
            for i in range(len(digits)):
                result.append(num_val//(10**(len(digits)-i-1)))
                num_val = num_val%(10**(len(digits)-i-1))
                
    else:
        for i in range(len(digits)+1):
            result.append(num_val//(10**(len(digits)-i)))
            num_val = num_val%(10**(len(digits)-i-1))
            
    return result


TEST_CASE_1 = [1,9,9] # Expected: [2,0,0]
TEST_CASE_2 = [3,2] # Expected: [3,3]
TEST_CASE_3 = [9,9,9]   # Expected: [1,0,0,0]

print(plusOne(TEST_CASE_1))
print(plusOne(TEST_CASE_2))
print(plusOne(TEST_CASE_3))



            