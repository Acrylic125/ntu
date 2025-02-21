#include <stdio.h>
#include <string.h>
void strIntersect(char *str1, char *str2, char *str3);
int main()
{
    char str1[50],str2[50],str3[50];

    printf("Enter str1: \n");
    scanf("%s",str1);
    printf("Enter str2: \n");
    scanf("%s",str2);
    strIntersect(str1, str2, str3);
    if (*str3 == '\0')
        printf("strIntersect(): null string\n");
    else
        printf("strIntersect(): %s\n", str3);
    return 0;
}

void strIntersect(char *str1, char *str2, char *str3)
{
    int str1Length = strlen(str1);
    int str2Length = strlen(str2);

    int filledIndex = 0;

    for (int i = 0; i < str1Length; i++) {
        char cur = str1[i];
        for (int j = 0; j < str1Length; j++) {
            char compare = str2[j];
            if (cur == compare) {
                str3[filledIndex] = cur;
                filledIndex++;
                break;
            } 
        }
    }
    str3[filledIndex] = '\0';
} 
