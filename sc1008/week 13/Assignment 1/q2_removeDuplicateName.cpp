///////// Student Info/////////
//
//           Your Name: Tan Jun Zhi Benedict
//      Your NTU Email: BTAN138@e.ntu.edu.sg
//
//
//

#include <iostream>
#include <string>

struct StringNode {
  std::string name;
  StringNode *next;
};

void printList(const StringNode *head) {
  const StringNode *temp = head;
  while (temp) {
    std::cout << temp->name << " -> ";
    temp = temp->next;
  }
  std::cout << "NULL" << std::endl;
}

void append(StringNode *&head, const std::string &name) {
  StringNode *newNode = new StringNode;
  newNode->name = name;
  newNode->next = nullptr;
  if (!head) {
    head = newNode;
    return;
  }
  StringNode *temp = head;
  while (temp->next) {
    temp = temp->next;
  }
  temp->next = newNode;
}

void freeList(StringNode *&head) {
  while (head) {
    StringNode *temp = head;
    head = head->next;
    delete temp;
  }
}

// Remove duplicate names from the linked list
void removeDuplicatedNames(StringNode *&head) {
  StringNode *prev = head;
  StringNode *cur = head->next;

  while (cur != nullptr) {
    // Check from head to cur for duplicates.

    StringNode *curCheck = head;
    bool hasDupe = false;
    while (curCheck != nullptr) {
      // Check to cur, excluding cur.
      if (curCheck == cur) {
        break;
      }
      if (!curCheck->name.compare(cur->name)) {
        hasDupe = true;
        break;
      }
      curCheck = curCheck->next;
    }

    if (hasDupe) {
      StringNode *next = cur->next;
      prev->next = cur->next;
      StringNode *temp = cur;
      delete cur;
      cur = next;
    } else {
      prev = cur;
      cur = cur->next;
    }
  }
}

int main() {
  StringNode *head = nullptr;
  append(head, "Alice");
  append(head, "Alice");
  append(head, "Bob");
  append(head, "Charlie");
  append(head, "David");
  printList(head);
  removeDuplicatedNames(head);
  printList(head);
  freeList(head);

  return 0;
}
