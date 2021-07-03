// Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.



#include<iostream>
#include<vector>

using namespace std;

class Solution{
private:
	vector<int> num_vec;
	int win_size;

public:
	void movAverage(int size){
		win_size = size;
	}

	int next(int next_elem){
		if (num_vec.size() < win_size){
			num_vec.push_back(next_elem);
		}
		else{
			num_vec.erase(num_vec.begin(), num_vec.begin() + num_vec.size() - win_size + 2);
			num_vec.push_back(next_elem);
		}
		int sum = 0;
		for (int i = 0; i < win_size; i ++){
			sum = sum + num_vec[i];
		}

		return sum;
	}
};

int main(){
	Solution sol;
	sol.movAverage(3);
	sol.next(1);
	sol.next(2);
	sol.next(3);
	sol.next(4);
}