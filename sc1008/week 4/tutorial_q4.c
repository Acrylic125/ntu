#include <stdio.h>

#define SIZE 4

void printArray2D(int arr[][SIZE], int rowSize, int colSize) {
    for(int i = 0; i < rowSize; i++) {
        for(int j = 0; j < colSize; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
}

void add(int ar[], int size) {
    int k;
    for (k = 0; k < size; k++)
        ar[k]++;
}

int main() {

    int array[3][4];
    int h,k;
    for (h = 0; h < 3; h++)
        for (k = 0; k < 4; k++)
            array[h][k] = h + k + 69;

    printf("Before Add: \n\r");
    printArray2D(array, 3, SIZE);

    for (h = 0; h < 3; h++) /* line a */
        add(array[0], 4 * 3);
        // add(array[h], 4);

    printf("After Add: \n\r");
    printArray2D(array, 3, SIZE);

    return 0;
}

