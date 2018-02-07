# leetcode #681 Next Closest Time. Only difference is have to return only one mutation of each digit
def nextClosestTime(time):
	input_time = set(time)
	hour = int(time[0:2])
	minute = int(time[3:5])
	counter = 0
	while True:
		minute += 1
		if minute == 60:
			minute = 0
			hour = 0 if hour == 23 else hour + 1

		closest_time = "%02d:%02d" %(hour, minute)
		counter += 1

		if set(closest_time) <= input_time and unique_comp(closest_time, time):
			return closest_time

		if counter == 24 * 60 * 60:
			break
	return time

def unique_comp(time1, time2):
	time1_list = [int(time1[0]), int(time1[1]), int(time1[3]), int(time1[4])]
	time2_list = [int(time2[0]), int(time2[1]), int(time2[3]), int(time2[4])]
	return sorted(time1_list) == sorted(time2_list)

print(nextClosestTime("11:00"))