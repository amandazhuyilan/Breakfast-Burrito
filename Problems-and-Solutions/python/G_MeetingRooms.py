# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.

def meetingRooms(timeSlots):
	timeSlots = sorted(timeSlots, key=lambda x:x[0])
	# timeSlots = sorted(timeSlots)

	result = []
	for time in timeSlots:
		if len(result) == 0 or result[-1][-1] > time[0]:
			result.append(time)
		else:
			result[-1][-1] = max(result[-1][-1], time[-1])
	return len(result)

print(meetingRooms([[0, 30],[5, 10],[15, 20]]))
