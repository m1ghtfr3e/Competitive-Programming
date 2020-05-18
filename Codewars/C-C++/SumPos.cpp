// Pretty much the same as in C just with vector rather array

#include <iostream>
#include <vector>

using namespace std;

int positive_sum (const std::vector<int> arr);

int main(){

  vector<int> v;
  v = {1,2,3,4,-2,-6,4,-5,2};

  cout << positive_sum(v) << endl;

  return 0;
}


int positive_sum (const std::vector<int> arr){

    int size = arr.size();
    int sum = 0;

    for (int i = 0; i < size; i++){
        if ( arr[i] > 0){
            sum += arr[i];
        }
    }
    return sum;
}
