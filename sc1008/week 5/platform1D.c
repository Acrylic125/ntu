#include <stdio.h>
int platform1D(int ar[], int size);
int main()  
{
    int i,b[50],size;
    printf("Enter array size: \n");
    scanf("%d", &size);
    printf("Enter %d data: \n", size);
    for (i=0; i<size; i++)  
        scanf("%d",&b[i]);
    printf("platform1D(): %d\n", platform1D(b,size));
    return 0;
}

int platform1D(int ar[], int size)
{
    if (size <= 0) {
        return 0;
    }

    int longestPlatformSize = 0;
    int curPlatformSize = 0;
    int curPlatformId = ar[0];
    for (int i = 0; i < size; i++) {
        int id = ar[i];
        if (id == curPlatformId) {
            curPlatformSize++;
        } else {
            if (curPlatformSize > longestPlatformSize) {
                longestPlatformSize = curPlatformSize;
            }
            curPlatformSize = 1;
            curPlatformId = id;
        }
    }

    if (curPlatformSize > longestPlatformSize) {
        longestPlatformSize = curPlatformSize;
    }

    return longestPlatformSize;
}
