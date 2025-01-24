#include <stdio.h>

int main() {
    int salary;
    int merit;
    printf("Enter the salary:  \n\r");
    scanf("%d", &salary);
    printf("Enter the merit:  \n\r");
    scanf("%d", &merit);

    char grade = ' ';
    if (salary >= 700) {
        grade = 'A';
        if (salary <= 799 && merit < 20) {
            grade = 'B';
        }
    } else if (salary >= 600) {
        grade = 'B';
        if (salary <= 649 && merit < 10) {
            grade = 'C';
        }
    } else {
        grade = 'C';
    }
    
    printf("The grade: %c \n\r", grade);
    return 0;
}
