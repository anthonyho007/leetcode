#include <stdlib.h>
#include <string.h>

static int compare (const void **key1, const void **key2) {
    if ( *(*(const int**)key1) > *(*(const int**)key2)) {
        return 1;
    }
    else if ( *(*(const int**)key1) < *(*(const int**)key2)) {
        return -1;
    }
    else {
        return 0;
    }
}

int* twoSum(int* nums, int numsSize, int target) {
    int i = 0;
    int j = numsSize -1;
    int* result;
    int **array;
    array = (int **)malloc(sizeof(int*)*numsSize);
    for (int x = 0; x < numsSize; x++) {
        array[x] = (int *)malloc(sizeof(int)*2);
        *(*(array+x)) = nums[x];
        *(*(array +x)+1) = x;
    }
    result=(int *)malloc(sizeof(int) *2);
    qsort(array, numsSize, sizeof(int**), compare);    
    while ( i < j ) {
        while ( array[i][0] + array[j][0] <= target && i < j) {
            if (array[i][0] + array[j][0] == target && i != j) {
                result[0]= array[i][1];
                result[1] = array[j][1];
                free(array);
                return result;
            }
            i++;
        }
        j--;
        while ( array[i][0] + array[j][0] >= target && i < j) {
            if (array[i][0] + array[j][0] == target && i != j) {
                result[0] = array[i][1];
                result[1] = array[j][1];
                free(array);
                return result;
            }
            j--;
        }
    }
    free(array);
    return result;
}  