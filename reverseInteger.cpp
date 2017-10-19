#include <stdlib.h>
#include <limits.h>

int addO( int *result, int x, int y){
	if ( x > INT_MAX - y){
		return -1;
	}
	else {
		*result = x + y;
		return 0;
	}
}


int mulO( int *result, int x, int y){
	*result = x * y;
	if ( x > INT_MAX / y) {
		return -1;
	}
	else 
		*result = x * y;
		return 0;
}

class Solution {
public:
	int reverse(int x){
		int num;
		int sign = 0;
		if ( x < -1){
			num = abs(x);
			sign = 1;
		}
		else {
			num	= x;
		}
		int* result = (int *)malloc(sizeof(int));
		*result = 0;
		while (num > 0){
			if ( mulO( result, *result, 10) == -1)
				return 0;
			if ( addO( result, *result, num%10) == -1)
				return 0;
			num /= 10; // overflow safe
		}
		if ( sign == 1 )
			*result *= -1;
		return *result;
	}
};