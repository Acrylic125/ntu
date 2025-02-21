#include <stdio.h>
#include <string.h>
#define N 20
void largeCharStr(char str[N][20], char a[N], int size);
int main()
{
    char str[N][20],dummy;
    char a[N],i,j,size;

    printf("Enter number of strings: \n");
    scanf("%d", &size);
    scanf("%c", &dummy);
    for (i=0;i<size;i++){
        printf("Enter string %d: \n", i+1);
        scanf("%s",str[i]);
    }
    largeCharStr(str,a,size);
    printf("largeCharStr(): \n");
    for (i=0;i<size;i++) {
        printf("String %d: ",i+1);
        printf("%c\n",a[i]);
    }
    return 0;
}

void largeCharStr(char str[N][20], char a[N], int size)
{
    for (int i = 0; i < size; i++) {
        char *cur = str[i];
        if (strlen(cur) <= 0) {
            continue;
        }

        char largestInStr = cur[0];
        int j = 0;
        while (1) {
            char c = cur[j];
            if (c == '\0') {
                break;
            }

            if (largestInStr < c) {
                largestInStr = c;
            }
            j++;
        } 

        a[i] = largestInStr;
    }
}
