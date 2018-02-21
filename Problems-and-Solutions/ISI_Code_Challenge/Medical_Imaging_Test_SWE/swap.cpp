#include <stdio.h>
#include <iostream>

using namespace std;

void swap(int* array, int n){
	int i = 0;
	int temp;
	

	// Argument edge cases testing for empty array and n = 0
	if(!array) {
		cerr << "Array does't exist!" << endl;
		return;

	}
	if(n <= 0) {
		cerr << "Invalid input array size!" <<  endl;
		return;
	}


	while (i < n){
		temp = *(array + i);
		*(array + i) = *(array + n - 1);
		*(array + n - 1) = temp;
		n--;
		i++;
	}
}

int main(){
	int input[6] = {1,2,3,4,5,6};
	int *array = input;
	cout << "original array is:";

	for (int i = 0; i < 6; i++){
		cout << *(array + i) << " ";
	}
	cout << endl;

	swap(array, 6);

	cout << "swapped array is:";
	for (int i = 0; i < 6; i++){
		cout << *(array + i) << endl;
	}
	cout << endl;

	return 0;

}