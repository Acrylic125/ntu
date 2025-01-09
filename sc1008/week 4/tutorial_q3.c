#include <stdio.h>

#define SIZE 4

void reduceMatrix2D(int arr[][SIZE], int rowSize, int colSize) {
    for (int i = 0; i < colSize; i++) {
        int s = 0;
        for (int j = i; j < rowSize; j++) {
            s += arr[j][i];
            arr[j][i] = 0;
        }
        arr[i][i] = s;
    }
}

void printArray2D(int arr[][SIZE], int rowSize, int colSize) {
    for(int i = 0; i < rowSize; i++) {
        for(int j = 0; j < colSize; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int arr[SIZE][SIZE] = {
        {
            1, 2, 3, 4
        }, {
            5, 6, 7, 8
        }, {
            9, 10, 11, 12
        }, {
            13, 14, 15, 16
        }
    };

    printf("Before Reduction: \n\r");
    printArray2D(arr, SIZE, SIZE);
    reduceMatrix2D(arr, SIZE, SIZE);
    printf("After Reduction: \n\r");
    printArray2D(arr, SIZE, SIZE);

    return 0;
}
