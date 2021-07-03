# leetcode #683 K empty slots. Only difference is have to return the latest day number for when there is k continuous empty slots

class Solutions:
	def kEmptySlots(self, flowers, k):
		N = len(flowers)
		if k > N - 2 or N < 3:
			return -1
		garden = [[ None ] * N ] * N
		inspect = flowers[::-1]

		row = N - 1
		for i in inspect:
			garden[row][i-1] = 0
			if garden[row][:].count(0) > k:
				index_list = []
				for index, n in enumerate(garden[row][:]):
					if n == 0:
						index_list.append(index+1)
					if index == 0 or index == N:
						break
				if self.ifContinue(index_list,k):
					return row + 1
				else:
					continue
			row = row - 1
		return -1 

	def ifContinue(self, input_list, k):
		input_list = sorted(input_list)
		diff = []
		for index in range(len(input_list)-1):
			diff.append(input_list[index+1]-input_list[index])
		if diff.count(1) == k - 1:
			return True
		else:
			return False


# flowers = [3,1,5,4,2]
# k = 2

flowers = [3,1,5,4,2]
k = 1

print(Solutions().kEmptySlots(flowers,k))

