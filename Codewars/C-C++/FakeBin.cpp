#include <string>
#include <iostream>
using namespace std;

string fakeBin(string str);

int main(){
    string str;
    str = "45385593107843568";

    string solution = fakeBin(str);
    cout << solution << endl;
    return 0;
}


string fakeBin(string str){
  // If n < 5 -> 0; n >= 5 -> 1
  int size = str.size();
  for (int i = 0; i < size; i++){
      if (str[i] < '5'){
        str[i] = '0';
      }
      else {
        str[i] = '1';
      }
  }
  return str;
}
