#include <stdio.h>
void rPattern1(int height);
int main()
{
 int height;
 printf("Enter height: \n");
 scanf("%d", &height);
 rPattern1(height);
 return 0;
}

void rPattern1(int height)
{
    if (height <= 0) {
        return;
    }
    rPattern1(height - 1);

    for (int i = 0; i < height; i++) {
        printf("*");
    }
    printf("\n\r");
}
