#include <stdio.h>
int reverseDigits(int num);

int main() {
    int num, result = 999;
    printf("Enter a number: \n");
    scanf("%d", &num);      
    printf("reverseDigits(): %d\n", reverseDigits(num));
    return 0;
}

int reverseDigits(int num) {
    int m = 1;
    int remainder = num;
    while (1) {
        m *= 10;
        remainder /= 10;
        if (remainder <= 0) {
           break; 
        }
    }

    int reversed = 0;
    remainder = num;
    while (1) {
        int digit = remainder % 10;
        remainder /= 10;

        m /= 10;
        reversed += (digit * m);

        if (remainder <= 0) {
           break; 
        }
    }
    return reversed;
}

