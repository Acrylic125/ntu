#include <stdio.h>
void rFindMaxAr(int *a, int size, int *max);
int main()
{
 int ar[50],i,max,size;

 printf("Enter array size: \n");
 scanf("%d", &size);
 printf("Enter %d numbers: \n", size);
 for (i=0; i < size; i++)
 scanf("%d", &ar[i]);
 max=ar[0];
 rFindMaxAr(ar,size,&max);
 printf("rFindMaxAr(): %d\n", max);
 return 0;
}

void rFindMaxAr(int *ar, int size, int *max)
{
    if (size <= 0) {
        return;
    }

    if (size == 1) {
        *max = *ar;
        return;
    }

    rFindMaxAr(
            1 + ar,
            size - 1,
            max
            );
    int cur = *ar;
    if (cur > *max) {
        *max = cur;
    }
}
