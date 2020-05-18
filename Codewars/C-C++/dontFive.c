#include <stdio.h>

int dontGiveMeFive(int start, int end);


int main(){

  int start = -9;
  int end = -1;
  unsigned answer = dontGiveMeFive(start, end);

  printf("%d\n", answer);

  return 0;
}

int dontGiveMeFive(int start, int end){
  // unsigned because of negative input number; range can not be negative
  unsigned range = end+1 - start;
  int countFive = 0;

  for (int i = start; i < end+1; i++){
    if (i % 5 == 0 && i % 2 != 0){
      countFive++;
    }
  }
  //printf("%d", countFive);
  unsigned diff = range - countFive;
  return diff;
}
