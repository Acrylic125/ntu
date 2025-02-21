#include <stdio.h>
#define M 80
int mergeArrays(int a[M], int b[M], int c[M], int n1, int n2);
int main()
{
    int a[M],b[M],c[M],i,k=0,n1,n2;
    printf("Enter the size of array a: \n");
    scanf("%d", &n1);
    printf("Enter the size of array b: \n");
    scanf("%d", &n2);
    printf("Enter array a[%d]: \n", n1);
    for (i=0; i<n1; i++)
        scanf("%d",&a[i]);
    printf("Enter array b[%d]: \n", n2);
    for (i=0; i<n2; i++)
        scanf("%d",&b[i]);
    k=mergeArrays(a,b,c,n1,n2);
    printf("mergeArrays(): \n");
    for (i=0;i<k;i++)
        printf("%d ",c[i]);
    return 0;
}

int mergeArrays(int a[M], int b[M], int c[M], int n1, int n2)
{
    int aI = 0;
    int bI = 0;

    int mI = 0;
    while (1) {
        if (mI >= 80) {
            break;
        }

        if (aI >= n1 && bI >= n2) {
            break;
        } else if (aI >= n1 && bI < n2) {
            int bVal = b[bI++];
            c[mI++] = bVal;
        } else if (aI < n1 && bI >= n2) {
            int aVal = a[aI++];
            c[mI++] = aVal;
        } else {
            int aVal = a[aI];
            int bVal = b[bI];
            
            if (aVal >= bVal) {
                c[mI++] = bVal;
                bI++;
            } else {
                c[mI++] = aVal;
                aI++;
            }
        }
    }
    return mI;
} 
