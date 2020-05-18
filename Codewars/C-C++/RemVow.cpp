#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>


std::string disemvowel(std::string str);

int main(){

  std::string str;

  str = "Let us see which letters will remain";

  std::cout << "original string: \n" << str << "\n" << std::endl;
  std::cout << "without vowels: \n" << disemvowel(str) << std::endl;

  return 0;
}


std::string disemvowel(std::string str){
      // Define the vowels in a string
      std::string vowels = "aAeEiIoOuU";

      for (char c: vowels){
        str.erase(std::remove(str.begin(), str.end(), c), str.end());
      }
      return str;
}
