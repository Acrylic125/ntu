#include <stdio.h>

int main()
{
    /* Write your program code here */

    printf("Enter the values for a1, b1, c1, a2, b2, c2: \r\n");
    double a1, b1, c1, a2, b2, c2;

    scanf("%lf %lf %lf %lf %lf %lf", &a1, &b1, &c1, &a2, &b2, &c2);

    printf("a1 = %.2f, b1 = %.2f, c1 = %.2f, a2 = %.2f, b2 = %.2f, c2 = %.2f \r\n", a1, b1, c1, a2, b2, c2);
    double x = (b2 * c1 - b1 * c2) / (a1 * b2 - a2 * b1);
    double y = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1);

    printf("x = %.2f, y = %.2f \r\n", x, y);

    return 0;
} 
