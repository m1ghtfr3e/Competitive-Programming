#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

//int addSum(int num);


int main() {

    int n;
    scanf("%d", &n);
		int num, sum = 0;

		while (n > 0){
			num = n % 10;
			sum += num;
			n /= 10;
		}

		printf("%d", sum);

    return 0;
}
