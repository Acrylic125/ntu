#include <stdio.h>
#include <string.h>

char *sweepSpace1(char *str);
char *sweepSpace2(char *str);
int main() {
    char str[80],str2[80], *p;

    printf("Enter the string: \n");
    fgets(str, 80, stdin);
    if (p = strchr(str,'\n')) {
        *p = '\0';
    }
    strcpy(str2,str);
    printf("sweepSpace1(): %s\n", sweepSpace1(str));
    printf("sweepSpace2(): %s\n", sweepSpace2(str2));
    return 0;
}

char *sweepSpace1(char *str) {
    int newStrCursor = 0;
    int lastI = 0;
    int length = strlen(str);
    if (length == 0) {
        return str;
    }

    int numOfSpaces = 0;
    for (int i = 0; i < length; i++) {
        char curCHar = str[i];

        if (curCHar == ' ') {
            numOfSpaces++;
        }
        if (curCHar == '\0') {
            break;
        }
    }

    for (int i = 0; i < length; i++) {
        char curCHar = str[i];

        lastI = i;
        if (curCHar != ' ') {
            str[newStrCursor++] = curCHar;
        }
        if (curCHar == '\0') {
            break;
        }
    }

    str[length - numOfSpaces] = '\0';

    return str;
}

char *sweepSpace2(char *str) {
    int newStrCursor = 0;
    int lastI = 0;
    int length = strlen(str);
    if (length == 0) {
        return str;
    }

    int numOfSpaces = 0;
    for (int i = 0; i < length; i++) {
        char curCHar = *(str + sizeof(char) * i);

        if (curCHar == ' ') {
            numOfSpaces++;
        }
        if (curCHar == '\0') {
            break;
        }
    }

    for (int i = 0; i < strlen(str); i++) {
        char curCHar = *(str + sizeof(char) * i);

        if (curCHar != ' ') {
            *(str + sizeof(char) * newStrCursor++) = curCHar;
        }
        if (curCHar == '\0') {
            break;
        }
    }

    str[length - numOfSpaces] = '\0';

    return str;
} 
