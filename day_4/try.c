#include<stdio.h>
struct MyStruct {
  int a;
  char b;
};

int main() {
  struct MyStruct s1 = {1, 'a'};
  struct MyStruct s2 = {1, 'b'};

  int result = memcmp(&s1, &s2, sizeof(struct MyStruct));
  printf("%d",result);
  if (result == 0) {
    printf("The structures are equal.\n");
  } else {
    printf("The structures are not equal.\n");
  }

  return 0;
}
