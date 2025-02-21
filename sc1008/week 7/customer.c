#include <stdio.h>
#include <string.h>
struct account {    
    struct
    {   
        char lastName[10];
        char firstName[10];
    } names;
    int accountNum;
    double balance;
};
void nextCustomer(struct account *acct);
void printCustomer(struct account acct);
int main()
{    
    struct account record;
    int flag = 0;
    do {   
        nextCustomer(&record);
        if ((strcmp(record.names.firstName, "End") == 0) &&
                (strcmp(record.names.lastName, "Customer") == 0))
            flag = 1;
        if (flag != 1)           
            printCustomer(record);
    } while (flag != 1);
}

void nextCustomer(struct account *acct)    
{   
    printf("Enter names (firstName lastName):  \n\r");
    char fullName[21];
    fgets(fullName, sizeof(fullName), stdin);

    char *p;
    p = strchr(fullName, '\n');
    if (p) {
        *p = '\0';
    }

    if (strcmp(fullName, "End Customer") == 0) {
        strcpy(acct->names.firstName, "End");
        strcpy(acct->names.lastName, "Customer");
        return;
    }

    // Trim leading space.
    char *fullNameStart = fullName;
    while (1) {
        if (*fullNameStart != ' ') {
            break;
        }
        fullNameStart = (fullNameStart + 1);
    }

    char* lastNamePtr = strchr(fullNameStart, ' ');
    // If last name ptr was not set, then ignore last name
    if (lastNamePtr) {
        *lastNamePtr = '\0';
        int firstNameLength = strlen(fullNameStart);
        if (firstNameLength > 9) {
            firstNameLength = 9;
        }
        strncpy(acct->names.firstName, fullNameStart, firstNameLength);
        acct->names.firstName[firstNameLength] = '\0';
        int firstLength = strlen(acct->names.firstName);
        while (firstLength > 0) {
            if (acct->names.firstName[firstLength - 1] != ' ') {
                break;
            }
            firstLength--;;
        }
        acct->names.firstName[firstLength] = '\0';

        lastNamePtr++;
        while (1) {
            if (*lastNamePtr != ' ') {
                break;
            }
            lastNamePtr = (lastNamePtr + 1);
        }

        int lastNameLength = strlen(lastNamePtr);
        if (lastNameLength > 9) {
            lastNameLength = 9;
        }
        strncpy(acct->names.lastName, lastNamePtr, lastNameLength);
        acct->names.lastName[lastNameLength] = '\0';
        int lastLength = strlen(acct->names.lastName);
        while (lastLength > 0) {
            if (acct->names.lastName[lastLength - 1] != ' ') {
                break;
            }
            lastLength--;
        }
        acct->names.lastName[lastLength] = '\0';

    }


    printf("Enter account number:  \n\r");
    scanf("%d", &acct->accountNum);

    printf("Enter balance:  \n\r");
    scanf("%lf", &acct->balance);

    char dummy[80];
    fgets(dummy, 80, stdin);
}

void printCustomer(struct account acct)    
{   
    printf("Customer record:  \n\r");
    printf("%s %s %d %.2lf\n\r", acct.names.firstName, acct.names.lastName, acct.accountNum, acct.balance);
}
