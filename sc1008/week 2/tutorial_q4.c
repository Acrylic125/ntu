#include <stdio.h>

int main() {
    int factorials[10] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};

    double x = 0;
    scanf("%lf", &x);

    double eToTheX = 1;
    double xAcc = 1;
    for (int i = 1; i <= 10; i++) {
        xAcc *= x;
        eToTheX += xAcc / factorials[i];
        // xAcc = pow(x, i);
    }
    printf("e^%.2f = %.2f \r\n", x, eToTheX);

    return 0;
}
