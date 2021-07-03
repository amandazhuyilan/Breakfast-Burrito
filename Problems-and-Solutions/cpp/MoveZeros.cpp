#include <iostream>
#include <vector>

using namespace std;

class Solution{
public:
	void moveZeros(vector<int> & nums){
		vector<int> results;
		int non_zero_counter = 0;
		for (int i = 0; i < nums.size(); i++){
			if (nums[i] != 0){
				results.push_back(nums[i]);
				non_zero_counter ++;
			} 
		}

		for (int i = 0; i < nums.size() - non_zero_counter; i++){
			results.push_back(0);
		}

		cout << "final vector: ";
		for (auto i: results){
			cout << i << " ";
		}
		cout << endl;
	}
};

int main(){
	Solution sol;
	vector<int> vect{0,1,0,0,2};
	sol.moveZeros(vect);
}