#include <stdio.h>

#define INIT_VALUE 999
int extEvenDigits1(int num);
void extEvenDigits2(int num, int *result);
int main()
{
   int number, result = INIT_VALUE;
    
   printf("Enter a number: \n");
   scanf("%d", &number);
   printf("extEvenDigits1(): %d\n", extEvenDigits1(number));         
   extEvenDigits2(number, &result);
   printf("extEvenDigits2(): %d\n", result);
   return 0;
}

int extEvenDigits1(int num) {   
    int digits = 0;
    int remainder = num;
    int i = 1;

    char hasEven = 0;

    while (1) {
        int lastDigit = remainder % 10;
        remainder /= 10;

        if (lastDigit % 2 == 0) {
            digits += (lastDigit * i);
            i *= 10;
            hasEven = 1;
        }

        if (remainder <= 0) {
           break; 
        }
    }

    if (hasEven == 0) {
        return -1;
    }

    return digits;
}

void extEvenDigits2(int num, int *result) {   
    *result = extEvenDigits1(num);
}
