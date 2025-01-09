#include <stdio.h>
#include <stdlib.h>

void collectFrequency(int frequencies[], size_t size) {
    for (int i = 0; i < size; i++) {
        int n = rand() % 100;
        frequencies[i] = n;
    }
}

int main() {
    int n;
    scanf("%d", &n);
    
    int arr[n];
    collectFrequency(arr, n);

    float bucketSize = 100.0 / n;
    for (int i = 0; i < n; i++) {
        double min = (bucketSize * i);
        double max = (bucketSize * (1 + i) - 0.01);
        printf("%.2lf-%.2lf", min, max);
        int frequency = arr[i];
        for (int j = 0; j < frequency; j++) {
            printf("*");
        }
        printf("\n\r");
    }

    return 0;
}
