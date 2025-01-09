#include <stdio.h>
#include <math.h>

void inputXY(double *x1, double *y1, double *x2, double *y2) {
    printf("Input x1 y1 x2 y2: ");
    scanf("%lf %lf %lf %lf", x1, y1, x2, y2);
}

void outputResult(double dist) {
    printf("%lf", dist);
}

double calDistance1(double x1, double y1, double x2, double y2) {
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
}

void calDistance2(double x1, double y1, double x2, double y2, double *dist) {
    double res = calDistance1(x1, y1, x2, y2);
    *dist = res;
}

int main() {
    double x1, y1, x2, y2, distance=-1;
    inputXY(&x1, &y1, &x2, &y2); // call by reference
    distance = calDistance1(x1, y1, x2, y2); // call by value
    printf("calDistance1(): ");
    outputResult(distance);
    calDistance2(x1, y1, x2, y2, &distance); // call by reference
    printf("calDistance2(): ");
    outputResult(distance); // call by value
    return 0;
}
