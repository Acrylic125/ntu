// Example program
#include <iostream>
#include <string>

int main() {
  std::string line;
  std::cout << "Type a number: ";
  getline(std::cin, line);

  char *p;
  long converted = strtol(line.c_str(), &p, 10);
  std::cout << "It is: " << converted << "!\n";
  std::cout << "Char p: " << p << "!\n";
}
