#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char *even_or_odd(int number);


int main(){

  int number;
  char state[5];

  printf("Enter a number: \n");
  scanf("%d", &number);

  printf("%s", even_or_odd(number));
  return 0;
}


const char *even_or_odd(int number){
    char *odd = (char*) malloc(3);
    char *even = (char*) malloc(4);
    strcpy(odd, "Odd\n");
    strcpy(even, "Even\n");

    if ((number % 2) == 0){
      return even;
    }
    else{
      return odd;
    }
}
