#include <stdio.h>

int better_than_average(int class_points[], int class_size, int your_points);


int main(){

    int class_points[] = {2, 3};
    int class_size = sizeof(class_points) / sizeof(class_points[0]);
    int your_points = 5;

    int solution = better_than_average(class_points, class_size, your_points);
    if (solution == 0){
      printf("false");
    }
    else {
      printf("true");
    }

    return 0;
}


int better_than_average(int class_points[], int class_size, int your_points) {
      int sum = 0;
      for (int i = 0; i < class_size; i++){
          sum += class_points[i];
      }
      int average = ((sum + your_points) / (class_size+1));
      
      if (average < your_points){
          return 1;
      }
      else {
          return 0;
      }
}
