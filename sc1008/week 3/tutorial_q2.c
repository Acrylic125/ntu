#include <_ctype.h>
#include <stdio.h>
#include <math.h>

int digitValue1(int num, int k) {
    int m2 = pow(10, k - 1);
    int m = m2 * 10;
    int remainder = num % m;
    return remainder / m2;
}

void digitValue2(int num, int k, int *result) {
    int m2 = pow(10, k - 1);
    int m = m2 * 10;
    int remainder = num % m;
    int res = remainder / m2;
    (*result) = res;
}

int main() {
    int num;
    int k;
    printf("Enter the number: \n");
    scanf("%d", &num);
    printf("Enter k position: \n");
    scanf("%d", &k);

    int result = digitValue1(num, k);
    printf("digitValue(): %d\n", result);
    
    int _temp = 69;
    int *result2 = &_temp;
    digitValue2(num, k, result2);
    printf("digitValue2(): %d\n", *result2);

    return 0;
}
