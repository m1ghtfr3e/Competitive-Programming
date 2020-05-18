#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool is_square(int n);


int main(){
    int n;
    scanf("%d", &n);

    bool solution = is_square(n);
    printf("%s\n", solution ? "true" : "false");
}


bool is_square(int n) {
    double num = n;
    int root = sqrt(num);
    if ((root * root) == num){
        return true;
    }
    else {
        return false;
    }
}
