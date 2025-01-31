#include <stdio.h>

int main() {
    // printf("Type smth: ");
    //
    // char aStr[5];
    //
    // fgets(aStr, 5, stdin);
    // fputs(aStr, stdout);
    char aStr[] = {
        'a', 'b', 'c', '\0', 'd', 'e'
    };
    fputs(aStr, stdout);
    return 0;
}
