# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.

def validPalindrome(input_string):
	if input_string is None:
		return None

	string_list = []
	for i in input_string:
		string_list.append(i)

	for i in range(len(string_list)):
		element = string_list[i]
		del string_list[i]

		if isPanlindrome(string_list) is True:
			return True
		else:
			string_list.insert(i,element)

	if isPanlindrome(string_list) is False:
		return False

def isPanlindrome(input_string):
	if input_string is None:
		return None
	start = 0 
	end = len(input_string) - 1

	while start < end:
		if input_string[start] != input_string[end]:
			return False
		else:
			start += 1
			end -= 1
	return True 

print(validPalindrome("abbga"))
