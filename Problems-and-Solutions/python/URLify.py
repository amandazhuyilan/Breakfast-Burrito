# Replace all spaces in a string with "%20", with given the "true" length 
# of the string.

# Python strings are immutable, thus the only way to solve it is to 
# create a new string with the %20 added in it 

def URLify(input_str):
	space_index = [0]
	result_str = None

	for i, item in enumerate(input_str):
		if item == " ":
			space_index.append(i)

	# get the first word into the result
	result_str = input_str[0:space_index[1]] + "%20"

	for n, index in enumerate(space_index, start = 1):
		if n == len(space_index) - 1:
			break		

		else:
			result_str = result_str + input_str[(space_index[n]+1):(space_index[n+1])]+ "%20"


 	# add in the last word into result
 	result_str = result_str + input_str[(space_index[-1]+1): len(input_str)]

 	return result_str

TEST_CASE = "This is a string"
print(URLify(TEST_CASE))