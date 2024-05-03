//You are given an integer num. You can swap two digits at most once to get the maximum valued number.
// Return the maximum valued number you can get.
#include <vector>
using namespace std;

class Solution {
public:
    int maximumSwap(int num) {
        string numStr = to_string(num);
        int n = numStr.size();
        vector<int> maxIndex(n);
        iota(maxIndex.begin(), maxIndex.end(), 0);
        for (int i = n - 2; i >= 0; --i) {
            if (numStr[i] <= numStr[maxIndex[i + 1]]) {
                maxIndex[i] = maxIndex[i + 1];
            }
        }      
        for (int i = 0; i < n; ++i) {
            int j = maxIndex[i];
            if (numStr[i] < numStr[j]) {
                swap(numStr[i], numStr[j]);
                break;
            }
        }      
        return stoi(numStr);        
    }
};
