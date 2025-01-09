#include <stdio.h>

#define SIZE 4

void transpose2D(int arr[][SIZE], int rowSize, int colSize) {
    int copyArr[rowSize][colSize];
    for (int i = 0; i < rowSize; i++) {
        for (int j = 0; j < colSize; j++) {
            copyArr[i][j] = arr[i][j];
        }
    }

    for (int i = 0; i < rowSize; i++) {
        for (int j = 0; j < colSize; j++) {
            arr[i][j] = copyArr[j][i];
        }
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

    printf("Before Transposing: \n\r");
    printArray2D(arr, SIZE, SIZE);
    transpose2D(arr, SIZE, SIZE);
    printf("After Tranposing: \n\r");
    printArray2D(arr, SIZE, SIZE);

    return 0;
}
