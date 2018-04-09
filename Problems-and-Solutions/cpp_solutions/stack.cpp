// cpp implementation for a stack in a template
#include <iostream>
using namespace std;

#define MAX 100

template<class T>

class Stack{
private: 
	int top = -1;
public:
	T a[MAX];

	Stack(){};

bool push(T new_elem){
	if (top > MAX){
		cout << "top: " << top << endl;
		cout << "stack overflow in push()" << endl;
		return false;
	} 
	else{
		a[top++] = new_elem;
		cout << new_elem << " pushed!" << endl;
		return true;
	}
}

T pop(){
	if (top < 0){
		cout << "stack underflow in pop()" << endl;
		return 0;
	}
	else{
		T data = a[top--];
		cout << "popped: " << data << endl;
		return data;
	}
}

bool isEmpty(){
	return( top < 0); 
}
};

int main(){
	Stack<char> A;
	A.push('a');
	A.push('b');
	A.push('c');
	A.pop();
	return 0;
} 