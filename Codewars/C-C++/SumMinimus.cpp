// Not finished yet

#include <iostream>
#include <vector>
using namespace std;

//int sum_of_minimums(const vector<vector<int>> &numbers)



int main(){

  vector<vector<int>> numbers(4, vector<int>(4));
  numbers[3][5] = {
      {1,2,3,4,5},
      {5,6,7,8,9},
      {20,21,34,56,100}
    };

  cout << numbers << endl;



  return 0;
}
