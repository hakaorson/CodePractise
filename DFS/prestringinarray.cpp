
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
    vector<int> lexicalOrder(int n) {
        vector<int> res{};
        dfs(0, res, n);
        return res;
    }
    void dfs(int pre,vector<int>& res,int n) {
        for (int i = 0; i < 10; i++) {
            if (pre == 0 && i == 0)
                continue;
            int target = pre * 10 + i;
            if (target <= n) {
                res.push_back(target);
                dfs(target, res, n);
            }
        }
    }
};

int main() {
    //vector<string> inputstr{ "i", "love", "leetcode", "i", "love", "coding" };
    //int k = 1;
    //vector<string> topk = Solution().topKFrequent(inputstr, k);
    vector<int> res = Solution().lexicalOrder(13);
    return 0;
}