#include <iostream>

using namespace std;

class Student {
public:
  int id;
  string name;
  double gpa;

  Student(int id, string name, double gpa) {
    this->id = id;
    this->name = name;
    this->gpa = gpa;
  }
};

inline int fn(int test = 3) {
  if (test <= 0) {
    return 0;
  }
  return 1 + fn(test - 1);
}

int main() {

  Student s1(123, "Alice", 3.5);
  Student s2(100, "Bob", 4.0);
  Student &student = s2;
  cout << student.id << ", " << student.name << ", " << student.gpa << endl;
  cout << s2.id << ", " << s2.name << ", " << s2.gpa << endl;

  cout << "After changing the reference" << endl;
  student = s1;
  s1.gpa = 3.0;
  cout << student.id << ", " << student.name << ", " << student.gpa << endl;
  cout << s2.id << ", " << s2.name << ", " << s2.gpa << endl;
  // student.id = 125;
  // student.name = "Hellen";
  //
  // cout << s1.id << endl;
  // cout << s1.name << endl;
  // cout << s2.id << endl;
  // cout << s2.name << endl;

  return 0;
}
