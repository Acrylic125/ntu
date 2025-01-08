#include <stdio.h>

int main() {

    printf("Enter your characters (# to end): ");
    int numOfDigits = 0;
    int numOfAZ = 0;
    while (1) {
        char c = getchar();
        if (c == '#') {
            break;
        }

        if (c >= '0' && c <= '9') {
            numOfDigits++;
        } else if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
            numOfAZ++;
        }
    }
    printf("The number of digits: %d \r\n", numOfDigits);
    printf("The number of letters: %d \r\n", numOfAZ);

    return 0;
}
