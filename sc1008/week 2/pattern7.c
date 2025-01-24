#include <stdio.h>

int main() {
    printf("Enter the height:  \n\r");
    int height;
    scanf("%d", &height);

    printf("The pattern is:\n\r");
    for (int i = 1; i <= height; i++) {
        for (int j = height; j >= 1; j--) {
            if (j <= i) {
                printf("*");
            } else {
                printf(" ");
            }
        }
        printf("\n\r");
    }

    return 0;
}
