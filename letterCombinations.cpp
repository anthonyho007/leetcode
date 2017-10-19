#include <stdlib.h>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
  public:
    vector<string> letterCombinations(string digits);
}

vector<string> Solution::letterCombinations(string digits) {
  vector<string> result;
  if (digits.size() == 0) return result;
  vector<string> digit = { "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
  result.push_back("");
  for( int i = 0; i < digits.size(); i++) {
    int num = digits[i] - '0';
    vector<string> buffer;
    for(int j = 0; j < digit[num].size(); j++) {
      for(int k = 0; k < result.size(); k++)
        buffer.push_back(result[k] + digit[num][j]);
    }
    result.swap(buffer);
  }
  return result;
}

