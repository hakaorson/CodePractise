
#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <unordered_map>
#include <array>
#include <numeric>
#include <stack>
#include <string>
#include <map>
#include <queue>
using namespace std;
class Solution {
public:
    int reversePairs(vector<int>&& nums) {
        if (nums.size() == 0)
            return 0;
        vector<int> temp(nums);
        int result= sort(0, nums.size() - 1, nums, temp);
        return result;
    }
    int sort(int left, int right, vector<int>& nums, vector<int>& temp) {
        if (left == right)
            return 0;
        int middle = (left + right) / 2;
        int sortl= sort(left, middle, nums, temp);
        int sortr=sort(middle + 1, right, nums, temp);
        return (merge(left, right, middle, nums, temp) + sortl + sortr);
    }
    int merge(int left,int right,int middle, vector<int>& nums, vector<int>& temp) {
        int res = 0;
        for (int i = left; i <= right; i++) {
            temp[i] = nums[i];
        }
        int lindex = left;
        int rindex = middle + 1;
        int finalindex = left;
        while (lindex <= middle && rindex <= right) {
            if (temp[lindex] <= temp[rindex]) {
                nums[finalindex] = temp[lindex];
                finalindex++;
                lindex++;
            }
            else {
                nums[finalindex] = temp[rindex];
                finalindex++;
                rindex++;
                res += (middle - lindex + 1);
            }
        }
        while (lindex <= middle) {
            nums[finalindex] = temp[lindex];
            finalindex++;
            lindex++;
        }
        while (rindex <= right) {
            nums[finalindex] = temp[rindex];
            finalindex++;
            rindex++;
        }
        return res;
    }
};

int main() {
    //vector<string> inputstr{ "i", "love", "leetcode", "i", "love", "coding" };
    //int k = 1;
    //vector<string> topk = Solution().topKFrequent(inputstr, k);
    int res = Solution().reversePairs(vector<int>{7, 5, 6, 4});
    return 0;
}