#include <stdio.h>


int get_sum(int a , int b);

int main(){
   // Take example: 5, -1
   int solution;
   int num1, num2;
   num1 = 5;
   num2 = -1;
   solution = get_sum(num1, num2);

   printf("%d", solution);

   return 0;
}


int get_sum(int a, int b){
    int result = 0;

    if (a == b){
      return a;
    }

    if (a < b){
      for (int i = a; i<=b; i++){
          result += i;
      }
      return result;
    }
    if (a > b){
        for (int i = b; i<=a; i++){
          result += i;
        }
        return result;
    }
}
