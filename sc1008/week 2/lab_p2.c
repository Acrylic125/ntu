#include <stdio.h>

int main() {
    int lines;
    printf("Enter number of lines:  \n\r");
    scanf("%d", &lines);

    for (int i = 0; i < lines; i++) {
        printf("Enter line %d (end with -1):  \n\r", i + 1);
        float tally = 0;
        int count = 0;
        
        while (1) {
            int num;
            scanf("%d", &num);

            if (num == -1) {
                break;
            }

            if (num < 0) {
                continue;
            }
            count++;
            tally += num;
        }

        float average = tally / count;
        printf("Average = %.2f\n\r", average);
    }
    return 0;
}
