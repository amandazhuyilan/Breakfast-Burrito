# Given a time responded in the format "HH:MM", form the next closest time by 
# reusing the current digits. There is no limit on how many times a digit can be 
# reused.

# You may assume that the given input string is always valid. "01:34", "12:09" are 
# all valid. "1:34", "12:9" are all invalid.

# Example: 
# Input: "19:34"
# Output: "19:39"

# Input: "23:59"
# Output: "22:22"

def Next_Closest_Time_Brute_Force(input_time):
	time = []
	for i in input_time:
		if i >= 0 and i <= 9:
			print(i)


Next_Closest_Time_Brute_Force("12:56")
