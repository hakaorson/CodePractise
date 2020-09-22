#include <iostream>
#include <vector>
#include <tuple>
#include <string>
#include <map>
#include <sstream>
#include <algorithm>
#include <bitset>
#include <stack>
using namespace std;
class Solution {
public:
    int trap(vector<int>& height) {
        stack<pair<int,int>> st{};
        int res = 0;
        for (int i = 0; i < height.size();i++) {
            while (!st.empty() && st.top().second <= height[i]) {
                pair<int, int> cur = st.top();
                st.pop();
                if (st.empty())break;
                res += (min(height[i], st.top().second)-cur.second) * (i - st.top().first - 1);
            }
            st.push(pair<int, int>(i, height[i]));
        }
        return res;
    }
};
int main() {
    vector<int>nums{ 2,1,0,2,1,0,1,3,2,1,2,1 };
    Solution solu{};
    solu.trap(nums);
	return 0;
}