#include <iostream>
#include <memory>

class Shape {
    public:
        virtual double area() const = 0;
        virtual double perimeter() const = 0;
        virtual ~Shape() {}; 
};

class Rectangle : public Shape {
    public:
        double width;
        double length;

        Rectangle();
        Rectangle(double len, double wid) : width(wid), length(len) {}

        double area() const override {
            return width * length;
        };

        double perimeter() const override {
            return 2 * (width + length);
        }
};

class Circle : public Shape {
    public:
        double radius;

        Circle(double rad) : radius(rad) {}
        double area() const override {
            return 3.14 * radius * radius;
        }
        double perimeter() const override {
            return 2 * 3.14 * radius;
        }
};

class ShapeFactory {
    public:
        static std::unique_ptr<Shape> createRectangle (double length, double width) {
            return std::make_unique<Rectangle>(length, width);
        };

        static std::unique_ptr<Shape> createCircle (double radius) {
            return std::make_unique<Circle>(radius);
        }
};