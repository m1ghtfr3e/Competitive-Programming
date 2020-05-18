#include <stdio.h>


// Task: Sum positive elem in array

int positive_sum(const int *values, size_t count);


int main(){

    int array[] = {1,2,3,-2,4,5,-6,-4,-7};
    size_t size = sizeof(array) / sizeof(array[0]);
    printf("%d\n", size);

    int solution = positive_sum(array, size);

    printf("%d\n", solution);

    return 0;
}


int positive_sum(const int *values, size_t count){

    int sum = 0;

    for (int i = 0; i < count; i++){
          if (values[i] > 0){
              sum += values[i];
          }
    }
    return sum;
}
