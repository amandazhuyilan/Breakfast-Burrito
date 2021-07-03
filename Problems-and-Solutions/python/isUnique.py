# Determine if a string has all uniquue charaters
# Create a empty list and append the ASCII vaule for each character in 
# string after checking if the ASCII value already exists. If exists, 
# return false.

# Python does not have string, use array of characters. 
# int of character: ord('a')

# Time complexity O(n)

def isUnique(input_str):
# for ASCII characters 
	if len(input_str) > 128:
		return False

	char_list = []

	for i in input_str:
		char_int = ord(i)
		if char_int in char_list:
			return False
		else: char_list.append(char_int)

	return True

TEST_CASE = "abd"
print(isUnique(TEST_CASE))
