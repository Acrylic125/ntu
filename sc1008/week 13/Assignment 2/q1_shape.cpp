///////// Student Info/////////
//
//           Your Name: Tan Jun Zhi Benedict
//      Your NTU Email: BTAN138@e.ntu.edu.sg
//
//
//
#include <cmath> // For M_PI
#include <iostream>
#include <type_traits> // Required for std::is_abstract

// Abstract base class
class Shape {
protected:
  double area;

public:
  // TO-DO: Please implement the constructor, the destructor and the calArea()
  // function here
  Shape() {
    area = 0.0;
    std::cout << "Shape Constructor!" << std::endl;
  }

  virtual ~Shape() { std::cout << "Shape Destructor!" << std::endl; }

  // Member function to get the area
  double getArea() const { return area; }

  virtual void calArea() = 0;
};

// Derived class: Circle
class Circle : public Shape {
private:
  double radius;

public:
  // TO-DO: Please implement the constructor, the destructor and OVERRIDE the
  Circle(double r) : radius(r) {
    std::cout << "Circle Constructor!" << std::endl;
  }

  ~Circle() { std::cout << "Circle Destructor!" << std::endl; }

  // calArea() function here
  void calArea() override {
    area = M_PI * radius * radius;
    // std::cout << "Area of Circle: " << area << std::endl;
  }
};

// Derived class: Rectangle
class Rectangle : public Shape {
private:
  double width;
  double height;

public:
  Rectangle(double w, double h) : width(w), height(h) {
    std::cout << "Rectangle Constructor!" << std::endl;
  }

  ~Rectangle() { std::cout << "Rectangle Destructor!" << std::endl; }

  // TO-DO: Please implement the constructor, the destructor and OVERRIDE the
  // calArea() function here
  void calArea() override {
    area = width * height;
    // std::cout << "Area of Rectangle: " << area << std::endl;
  }
};

int main() {
  std::cout << std::boolalpha;
  std::cout << "Is Shape abstract? " << std::is_abstract<Shape>::value
            << std::endl
            << std::endl;

  Shape *shape1 = new Circle(5.0);
  Shape *shape2 = new Rectangle(4.0, 6.0);
  std::cout << std::endl;

  shape1->calArea();
  shape2->calArea();

  std::cout << "Area of Circle: " << shape1->getArea() << std::endl;
  std::cout << "Area of Rectangle: " << shape2->getArea() << std::endl;
  std::cout << std::endl;

  // Clean up
  delete shape1;
  delete shape2;

  return 0;
}
