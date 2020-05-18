#include <stdio.h>

/*
a = a + b
b = | a - b |
*/


void update(int *a,int *b) {
 
    int enda, endb;

    enda = *a + *b;
    if (*a < *b){
        endb = *b - *a;
    }
    else {
        endb = *a - *b;
    }
    //a = &enda;
    //b = &endb;

    printf("%d\n%d", enda, endb);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    //printf("%d\n%d", a, b);

    return 0;
}