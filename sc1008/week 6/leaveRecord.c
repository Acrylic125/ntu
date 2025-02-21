#include <stdio.h>
#define INIT_VALUE 1000 

typedef struct {
 int id; /* staff identifier */
 int totalLeave; /* the total number of days of leave allowed */
 int leaveTaken; /* the number of days of leave taken so far */
} leaveRecord; 

int mayTakeLeave(leaveRecord list[], int id, int leave, int n) {
    leaveRecord *record = NULL;
    for (int i = 0; i < n; i++) {
        leaveRecord _record = list[i];
        if (_record.id == id) {
            record = &_record;
            break;
        } 
    }
    if (record == NULL) {
        return 0;
    }
    int newTaken = (record->leaveTaken + leave);
    return newTaken <= record->totalLeave ? 1 : 0;
}

void getInput(leaveRecord list[], int *n) {
    printf("Enter the number of staff records:  \n\r");
    scanf("%d", n);
    for (int i = 0; i < *n; i++) {
        leaveRecord record;
        printf("Enter id, totalleave, leavetaken:  \n\r");
        scanf("%d %d %d", &record.id, &record.totalLeave, &record.leaveTaken);
        list[i] = record;
    } 
}

void printList(leaveRecord list[], int n) {
    puts("The staff list:  \n\r");
    for (int i = 0; i < n; i++) {
        leaveRecord record = list[i];
        printf("id = %d, totalleave = %d, leave taken = %d \n\r", record.id, record.totalLeave, record.leaveTaken);
    }
}

int main() {
    leaveRecord listRec[10];
    int len;
    int id, leave, canTake=INIT_VALUE;
    int choice;     

    printf("Select one of the following options: \n");
    printf("1: getInput()\n");
    printf("2: printList()\n");
    printf("3: mayTakeLeave()\n");
    printf("4: exit()\n");
    do {
        printf("Enter your choice: \n");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                getInput(listRec, &len);
                printList(listRec, len);
                break;
            case 2:
                printList(listRec, len);
                break;
            case 3:
                printf("Please input id, leave to be taken: \n");
                scanf("%d %d", &id, &leave);
                canTake = mayTakeLeave(listRec, id, leave, len);
                if (canTake == 1)
                    printf("The staff %d can take leave\n", id);
                else if (canTake == 0)
                    printf("The staff %d cannot take leave\n", id);
                else if (canTake == -1)
                    printf("The staff %d is not in the list\n", id);
                else
                    printf("Error!");
                break;
        }
    } while (choice < 4);
    return 0;
}
