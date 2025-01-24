#include <stdio.h>

int main() {
    while (1) {
        int studentId;
        printf("Enter Student ID:  \n\r");
        scanf("%d", &studentId);
        if (studentId == -1) {
            return 0;
        }

        int mark;
        printf("Enter Mark:  \n\r");
        scanf("%d", &mark);

        if (mark < 0 || mark > 100) {
            printf("%d is not a valid mark.", mark);
            continue;
        }
        
        char grade = ' ';
        if (mark <= 44) {
            grade = 'F';
        } else if (mark <= 54) {
            grade = 'D';
        } else if (mark <= 64) {
            grade = 'C';
        } else if (mark <= 74) {
            grade = 'B';
        } else {
            grade = 'A';
        }

        printf("Grade = %c\n\r", grade);
    }
    return 0;
}
