#include <stdio.h>
#include <string.h>

int main() {
  printf("Type smth: ");

  char dummy[80];
  int a;
  scanf("%d", &a);
  char input[80];
  fgets(dummy, 80, stdin);

  printf("Now type another thing:");

  fgets(input, 80, stdin);

  char *p = strchr(input, '\n');
  if (p != NULL) {
    *p = '\0';
  }

  printf("You typed: %s\n", input);

  return 0;
}
