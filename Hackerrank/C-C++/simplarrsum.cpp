#include <iostream>
#include <vector>

/*
 * Complete the simpleArraySum function below.
 */
 int simpleArraySum(std::vector<int> ar) {
     int sum = 0;
     for (int i = 0; i < ar.size(); i++){
       sum += ar[i];
     }
     return sum;
 }

int main(){
    int n = 5;
    int sum;
    std::vector<int> arr(n);

    for (int i=0; i<n; i++){
      std::cin >> arr[i];
    }

    sum = simpleArraySum(arr);
    std::cout << sum << std::endl;

    return 0;
}
