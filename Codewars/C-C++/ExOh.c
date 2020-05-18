#include <stdbool.h>
#include <string.h>
#include <stdio.h>

bool xo(const char* str);

int main(){
    const char test[] = "ooom";      // Testcase
    bool solution = xo(test);
    printf("%d\n", solution);
}


bool xo(const char* str){
  // size of our string
  int size = strlen(str);
  int countX = 0;           // Counts x and X
  int countO = 0;           // Counts o and O

  for (int i = 0; i<size; i++){
      if (str[i] == 'x' || str[i] == 'X'){
        countX++;
      }
      if (str[i] == 'o' || str[i] == 'O'){
        countO++;
      }
  }
  if (countX == countO){
    return true;
  }
  else{
    return false;
  }
}
