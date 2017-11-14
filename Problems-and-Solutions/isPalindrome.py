
def is_Palindrome_Recrusive(s):
	if s == "":
		return True
	if s[0] == s[-1]:
		return is_Palindrome_Recrusive(s[1:-1])

def is_Palindrome_Iteration(s):
	if s == "":
		return True
	for i in range(len(s)//2):
		if s[i] != s[-(i+1)]:
			return False
	return True 

TEST_CASE1 = "abuttuba"
TEST_CASE2 = "word"


print("Original string is:", TEST_CASE1)
print("Recursive method:",is_Palindrome_Recrusive(TEST_CASE1))
print("Iterative method:",is_Palindrome_Iteration(TEST_CASE1))
