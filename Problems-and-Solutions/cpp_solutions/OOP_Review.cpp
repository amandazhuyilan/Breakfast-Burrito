#include <iostream>
#include <vector>
// #include <string>

using namespace std;

class Shape{
protected:
	int width;
	int height;
public:
	virtual int getArea(){
		return width * height;
	}

	void setWidth(const int & width_input ){
		width = width_input;
	}

	void setHeight(const int & height_input ){
		height = height_input;
	 
	void operator=(Shape &shape_in){
		height = shape_in.height;
		width = shape_in.width;
	}
};

class Rectangle: public Shape{
public:
	int getArea(){
		return width * height;
	}
};

class Triangle: public Shape{
public:
	int getArea(){
		return width * height/2;
	}
};

int main(){
	Rectangle Rec;
	Triangle Tri;

	Shape myShape1;
	Shape myShape2;

	int width_1 = 2;
	int height_1 = 3;

	// Tri.setWidth(2);
	// Tri.setHeight(3);

	// Rec.setWidth(width);
	// Rec.setHeight(height);
	// cout << "Rectangle Area: " << Rec.getArea() << endl;

	// Tri.setWidth(width);
	// Tri.setHeight(height);
	// cout << "Triangle Area: " << Tri.getArea() << endl;
	
	myShape1.setHeight(height_1);
	myShape1.setWidth(width_1);

	myShape2 = myShape1;

	cout << myShape2.getArea() << endl;
	return 0;

}