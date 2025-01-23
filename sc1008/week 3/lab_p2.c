#include <stdio.h>

int digitPos1(int num, int digit) {
    int digits = 0;
    int remainder = num;
    while (1) {
        digits++;
        int lastDigit = remainder % 10;
        if (lastDigit == digit) return digits;
        remainder /= 10;
        if (remainder <= 0) {
           break; 
        }
    }
    return 0;
}

void digitPos2(int num, int digit, int *result) {
    *result = digitPos1(num, digit);
}

int main() {
    int number, digit, result=0;
    printf("Enter the number: \n");
    scanf("%d", &number);
    printf("Enter the digit: \n");
    scanf("%d", &digit);
    printf("digitPos1(): %d\n", digitPos1(number, digit));
    digitPos2(number, digit, &result);
    printf("digitPos2(): %d\n", result);
    return 0; 
}

