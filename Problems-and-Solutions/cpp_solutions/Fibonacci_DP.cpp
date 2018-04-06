// get the nth elememnt of the fibonacci sequence
#include<iostream>
#include <vector>
using namespace std;

class Solution{
public:
	int get_fib(int n){
		if (n < 2){
			return n;
		}

		vector<int> fib_vec(n + 1);
		fib_vec[0] = fib_vec[1] = 1;
		for (int i = 2; i < n + 1; i ++){
			fib_vec[i] = fib_vec[i - 2] + fib_vec[i - 1];
		}

		return fib_vec[n];
	}
};


int main(){
	Solution solution;
	cout << solution.get_fib(5) << endl;
	return 0;
}



