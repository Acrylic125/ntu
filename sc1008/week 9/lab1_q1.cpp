#include <iostream>

using namespace std;

// Function to get a valid int input
int getValidInt() {
  // char *p;
  // long converted = strtol(line.c_str(), &p, 10);
  char buf[50];
  while (true) {
    cin.getline(buf, 50);

    bool foundValid = false;
    bool isNeg = buf[0] == '-';

    int i = isNeg ? 1 : 0;
    int acc = 0;
    while (buf[i] != '\0') {
      if (isdigit(buf[i])) {
        acc *= 10;
        acc += (int)(buf[i] - '0');
        foundValid = true;
      } else {
        break;
      }
      i++;
    }
    if (foundValid) {
      if (isNeg)
        acc *= -1;
      return acc;
    }
    cout << "Invalid input! Please enter an integer: ";
  }
}

// Function to get a valid float input
float getValidFloat() {
  char buf[50];
  while (true) {
    cin.getline(buf, 50);

    bool foundValid = false;
    bool isNeg = buf[0] == '-';

    int i = isNeg ? 1 : 0;
    float acc = 0;
    float fracFactor = 0; // Sets to 1 when '.' is found.
    while (buf[i] != '\0') {
      if (isdigit(buf[i])) {
        if (fracFactor != 0) {
          fracFactor /= 10;
          acc += (fracFactor * (int)(buf[i] - '0'));
        } else {
          acc *= 10;
          acc += (int)(buf[i] - '0');
        }
        foundValid = true;
      } else if (buf[i] == '.') {
        fracFactor = 1;
      } else {
        break;
      }
      i++;
    }
    if (foundValid) {
      if (isNeg)
        acc *= -1;
      return acc;
    }
    cout << "Invalid input! Please enter a float: ";
  }
}

int main() {
  char name[50];  // Student name
  int studentID;  // Student ID
  float mathMark; // Math mark
  while (true) {
    // Get student name
    cout << "Enter student name (or enter '#' to exit): ";
    cin.getline(name, 50);
    // Check if user wants to exit
    if (strcmp(name, "#") == 0) {
      break;
    }
    // Get student ID
    cout << "Enter student ID (integer): ";
    studentID = getValidInt();
    // Get math mark
    cout << "Enter math mark (float): ";
    mathMark = getValidFloat();
    // Display student information
    cout << "\nStudent Information:\n";
    cout << "Name: " << name << endl;
    cout << "Student ID: " << studentID << endl;
    cout << "Math Mark: " << mathMark << endl;
    cout << "-------------------------\n";
  }
  cout << "Program exited successfully." << endl;
  return 0;
}
