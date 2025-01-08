#include <stdio.h>

int main() {
    printf("Specify the height of the triangle: ");

    int height = 0;
    while (1) {
        scanf("%d", &height);
        if (height <= 0 || height > 9) {
            printf("Please enter a number between 1 and 9: ");
        } else {
            break;
        }
    }

    printf("The height of the triangle is %d \r\n", height);
    int i = 1;
    for (i = 1; i <= height; i++) {
        int j = 0;
        int imod3 = i % 3;
        char c = (imod3 == 0 ? 3 : imod3) + '0';
        for (j = 0; j < i; j++) {
            printf("%c", c);
        }
        printf("\r\n");
    }

    return 0;
}
