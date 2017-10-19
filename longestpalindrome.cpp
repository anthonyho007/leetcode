#include <stdlib.h>
#include <string>

class Solution {
public:
	string longestPalindrome(string s);
};

string Solution::longestPalindrome(string s) {
	int size = s.size();
	int start = 0;
	int max_len = 1;
	int left, right, i;

	for (i = 0; i < size; i++){
		left = i -1;
		right = i;

		while ( left >= 0 && right < size && s[left] == s[right]) {
			if ( max_len < (right - left + 1)){
				start = left;
				max_len = right -left + 1;
			}
			left--;
			right++;
		}

		left = i -1;
		right = i + 1;
		while ( left >= 0 && right < size && s[left] == s[right]) {
			if ( max_len < (right -left + 1)) {
				start = left;
				max_len = right -left + 1;
			}
			left--;
			right++;
		}
	}
	string result = s.substr(start, max_len);
	return result;
}