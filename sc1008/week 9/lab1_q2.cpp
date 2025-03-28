#include <cmath>
#include <iostream>
using namespace std;
bool isZero(float num, float epsilon = 1e-6) {
  return fabs(num) < epsilon; // Check if num is very close to 0
}

template <typename T> T calculate(T a, T b, char op) {
  switch (op) {
  case '+':
    return a + b;
  case '-':
    return a - b;
  case '*':
    return a * b;
  case '/':
    if (isZero(b)) {
      cout << "Error: Division by zero!" << endl;
      return 0;
    }
    return a / b;
  }
  return a + b;
}

// TO-DO: Write Your Code Here
int main() {
  cout << "Addition (10 + 5): " << calculate(10, 5, '+') << endl;
  cout << "Subtraction (10.5 - 3.2): " << calculate(10.5, 3.2, '-') << endl;
  cout << "Multiplication (4 * 2): " << calculate(4, 2, '*') << endl;
  cout << "Division (10 / 2): " << calculate(10, 2, '/') << endl;
  cout << "Division (10.6 / 0.0): " << calculate(10.6, 0.0, '/') << endl;
  cout << "Division by zero (10 / 0): " << calculate(10, 0, '/') << endl;
  return 0;
}
