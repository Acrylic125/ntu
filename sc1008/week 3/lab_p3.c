#include <stdio.h>

int numDigits1(int num) {
    int digits = 0;
    int remainder = num;
    while (1) {
        digits++;
        remainder /= 10;
        if (remainder <= 0) {
           break; 
        }
    }
    return digits;
}

void numDigits2(int num, int *result) {
    *result = numDigits1(num);
}

int main() {
     int number, result=0;
     printf("Enter the number: \n");
     scanf("%d", &number);
     printf("numDigits1(): %d\n", numDigits1(number));
     numDigits2(number, &result);
     printf("numDigits2(): %d\n", result);
     return 0;
}
