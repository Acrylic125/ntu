#include <stdio.h>

int extOddDigits1(int num) {
    int acc = 0;
    int m = 0;

    while (1) {
        int lastDigit = num % 10;
        num = num / 10;
        
        if (lastDigit % 2 == 1) {
            m = m == 0 ? 1 : m * 10;
            acc += (m * lastDigit);
        }

        if (num <= 0) {
            if (m == 0) return -1;
            return acc;
        }
    }
}

void extOddDigits2(int num, int *result) {
    int res = extOddDigits1(num);
    *result = res;
}

int main() {
    int number;
    printf("Enter a number: \n");
    scanf("%d", &number);
    printf("extOddDigits1(): %d\n", extOddDigits1(number)); 
    int _temp = 69;
    int* result2 = &_temp;
    extOddDigits2(number, result2);
    printf("extOddDigits2(): %d\n", *result2); 

    return 0;
}
