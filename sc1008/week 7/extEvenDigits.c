#include <stdio.h>
void rExtEvenDigits(int num, int *evenPtr);
int main()
{
    int number, result;
    printf("Enter a number: \n");
    scanf("%d", &number);
    rExtEvenDigits(number, &result);
    printf("rExtEveneDigits(): %d\n", result);
    return 0;
}

void rExtEvenDigits(int num, int *evenPtr)
{
    if (num == num / 10 * 10)
        *evenPtr = -1;
    if (num == 0)
        return;
    int lastDigit = num % 10;
    rExtEvenDigits(num / 10, evenPtr);
    if (lastDigit % 2 == 0) {
        if (*evenPtr == -1)
            *evenPtr = lastDigit;
        else
            *evenPtr = *evenPtr * 10 + lastDigit;
    }
}

// void rExtEvenDigits(int num, int *evenPtr)
// {
//     if (num <= 0) {
//         if (*evenPtr == 0) {
//             *evenPtr = -1;
//         }
//         return;
//     }
//
//     int lastDigit = num % 10;
//     if (lastDigit % 2 == 0) {
//         int n = 1;
//         int temp = *evenPtr;
//         while (temp > 0) {
//             temp /= 10;
//             n *= 10;
//         }
//
//         *evenPtr += (lastDigit * n);
//     }
//     num /= 10;
//     rExtEvenDigits(num, evenPtr);
// }
