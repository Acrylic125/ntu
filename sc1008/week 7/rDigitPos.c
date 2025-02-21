#include <stdio.h>
int rDigitPos1(int num, int digit);
void rDigitPos2(int num, int digit, int *pos);
int main()
{
    int number, digit, result=0;
    printf("Enter the number: \n");
    scanf("%d", &number);
    printf("Enter the digit: \n");
    scanf("%d", &digit);
    printf("rDigitPos1(): %d\n", rDigitPos1(number, digit));
    rDigitPos2(number, digit, &result);
    printf("rDigitPos2(): %d\n", result);
    return 0;
}

int rDigitPos1(int num, int digit)
{
    if (num == 0) {
        if (digit == 0) {
            return 1;
        }
        return 0;
    }
    int lastDigit = num % 10;
    if (lastDigit == digit) {
        return 1;
    }
    num /= 10;
    int f = rDigitPos1(num, digit);
    if (f == 0) {
        return 0;
    }
    return f + 1;
}

void rDigitPos2(int num, int digit, int *pos)
{
    *pos = rDigitPos1(num, digit);
}
