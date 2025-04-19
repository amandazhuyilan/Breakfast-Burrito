#include <iostream>
#include "shape_factory.cpp"

void test_shape_factory();

int main() {
    std::cout << "Starting...." << std::endl;
    test_shape_factory();
    return 0;
}

void test_shape_factory() {
    std::cout << "==================== Start ShapeFactory ====================" << std::endl;
    auto rect = ShapeFactory::createRectangle(1.0, 2.0);
    std::cout << "Created Rectangle with area: " << rect->area() << std::endl;
    
    auto circle = ShapeFactory::createCircle(1.5);
    std::cout << "Created circle with area: " << circle->area() << std::endl;
    std::cout << "==================== End ShapeFactory ====================" << std::endl;

    std::cout << "==================== Start Simple RPC ====================" << std::endl;


}