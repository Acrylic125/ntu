#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>  
#include <stdbool.h>

struct LinkedListNode {
    int value;
    struct LinkedListNode* next;
};

struct LinkedList {
    struct LinkedListNode* first;
    size_t size;
};

void add(struct LinkedList *ll, int value) {
    struct LinkedListNode *node = malloc(sizeof(struct LinkedListNode));
    node->value = value;

    struct LinkedListNode *cur = ll->first;
    if (cur == NULL) {
        ll->first = node;
        return;
    }

    while (cur != NULL) {
        if (cur->next == NULL) {
            break;
        }
        cur = cur->next;
    }

    cur->next = node;
}

bool delete(struct LinkedList *ll, int value) {
    struct LinkedListNode *cur = ll->first;
    struct LinkedListNode *last = NULL;

    bool found = false;

    while (cur != NULL) {
        if (value == cur->value) {
            found = true;
            break;
        }
        last = cur; 
        cur = cur->next;
    }

    if (found) {
        if (last == NULL) {
            ll->first = cur->next;
        } else {
            last->next = cur->next;
        }
        free(cur);
    }

    return found;
}

bool has(struct LinkedList *ll, int value) {
    struct LinkedListNode *cur = ll->first;
    while (cur != NULL) {
        if (value == cur->value) {
            return true;
        }
        cur = cur->next;
    }
    return false;
}

void freeLinkedList(struct LinkedList *ll) {
    struct LinkedListNode *cur = ll->first;
    while (cur != NULL) {
        struct LinkedListNode *next = cur->next; // Store the next node
        free(cur); // Free the current node
        cur = next; // Move to the next node
    }
    free(ll); // Finally, free the linked list structure itself
}

struct LinkedList createLinkedList(int values[], size_t size) {
    struct LinkedListNode* first = malloc(sizeof(struct LinkedListNode));
    first->value = values[0];
    first->next = NULL;
    struct LinkedList ll = {
        first, size
    }; 

    struct LinkedListNode* cur = first;
    for (int i = 1; i < size; i++) {
        struct LinkedListNode* next = malloc(sizeof(struct LinkedListNode));
        next->value = values[i];
        next->next = NULL;

        cur->next = next;
        cur = next;
    }
    return ll;
}

int main() {

    int values[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    struct LinkedList ll = createLinkedList(values, sizeof(values) / sizeof(values[0]));

    printf("%d exists: %d\n\r", 5, has(&ll, 5));
    printf("%d exists: %d\n\r", 10, has(&ll, 10));
    printf("%d exists: %d\n\r", -3, has(&ll, -3));
    printf("%d exists: %d\n\r", -33, has(&ll, 33));

    printf("%d exists: %d\n\r", 2, has(&ll, 2));
    delete(&ll, 2);
    printf("%d exists (Deleted): %d\n\r", 2, has(&ll, 2));
    printf("%d exists: %d\n\r", 1, has(&ll, 1));
    delete(&ll, 1);
    printf("%d exists (Deleted): %d\n\r", 1, has(&ll, 1));
    delete(&ll, 1);
    printf("%d exists (Deleted): %d\n\r", -33, has(&ll, -33));

    add(&ll, 69);

    struct LinkedListNode *cur = ll.first;
    while (cur != NULL) {
        printf("Item: %d\n\r", cur->value);
        cur = cur->next;
    }
    
    freeLinkedList(&ll);
    return 0;
}
