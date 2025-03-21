#include <stdio.h>

void readInput(int *id, int *noOfHours, int *payRate);
double computeSalary1(int noOfHours, int payRate);  
void computeSalary2(int noOfHours, int payRate, double *grossPay);

int main()
{
    int id = -1, noOfHours, payRate;
    double grossPay;

    readInput(&id, &noOfHours, &payRate);      
    while (id != -1) {
        printf("computeSalary1(): ");
        grossPay = computeSalary1(noOfHours, payRate);
        printf("ID %d grossPay %.2f \n", id, grossPay);
        printf("computeSalary2(): ");
        computeSalary2(noOfHours, payRate, &grossPay);
        printf("ID %d grossPay %.2f \n", id, grossPay);
        readInput(&id, &noOfHours, &payRate);
    }
    return 0;
}

void readInput(int *id, int *noOfHours, int *payRate) {
    printf("Enter ID (-1 to end):  \n\r");
    scanf("%d", id);
    printf("Enter number of hours:  \n\r");
    scanf("%d", noOfHours);
    printf("Enter hourly pay rate:  \n\r");
    scanf("%d", payRate);
}    

double computeSalary1(int noOfHours, int payRate) {
    int overtimeHours = noOfHours - 160;
    int baseHours = noOfHours;
    if (baseHours > 160) {
        baseHours = 160;
    }

    double pay = payRate * baseHours;
    if (overtimeHours > 0) {
        pay += 1.5 * overtimeHours * payRate;
    }
    return pay;
}

void computeSalary2(int noOfHours, int payRate, double *grossPay) {
    *grossPay = computeSalary1(noOfHours, payRate);
} 
