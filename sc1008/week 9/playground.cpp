// Example program
#include <iostream>
#include <string>

using namespace std;

void test(int *&ref) {
  cout << *ref << "!" << endl;
  int val = 10;
  ref = &val;
}

int main() {
  int abc = 30;
  int *ptr = &abc;
  test(ptr);

  cout << *ptr << "!!!" << endl;
  // std::string line;
  // std::cout << "Type a number: ";
  // getline(std::cin, line);
  //
  // char *p;
  // long converted = strtol(line.c_str(), &p, 10);
  // std::cout << "It is: " << converted << "!\n";
  // std::cout << "Char p: " << p << "!\n";
}
