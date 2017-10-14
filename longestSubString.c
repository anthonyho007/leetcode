#include <stdlib.h>
#include <string.h>

int lengthOfLongestSubstring(char* s) {
    int size;
    if ((size=strlen(s)) == 0)
        return 0;
    int max = 1;
    int i;
    int max_char = 256;
    int *array;
    array = (int *)malloc(sizeof(int)*max_char);
    for (i = 0; i < max_char; i++){
        array[i] = -1;
    }
    int current = 1;
    array[s[0]] = 0;
    for (i = 1; i < size; i++){
        if (array[s[i]] == -1){
            current += 1;
        }
        else if ( i - current > array[s[i]]) { 
            current += 1;
        }
        else {
            if ( current > max){
                max = current;
            }
            current = i - array[s[i]];
        }
        array[s[i]] = i;
    }
    if ( current > max){
        max = current;
    }
    free(array);
    return max;
    
}