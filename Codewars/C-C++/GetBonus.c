// Not finished yet


#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>

typedef unsigned long long ull;

char *bonus_time(ull salary, bool bonus);

int main(){

  int salary;
  bool bonus;
  int nbool;

  scanf("%d", &salary);
  // Taking 0 or 1 as true or false
  scanf("%d", &nbool);
  // Initializing bool with our int
  bonus = nbool;
  printf("%d", salary);

  return 0;
}


char *bonus_time(ull salary, bool bonus){
  string new_sal[];
  char sign[] = '$';

  if (bonus == true){
    strcpy(new_sal, sign);
  }


  return new_sal;
}
