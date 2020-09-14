
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
struct Order {
    bool operator ()(const pair<string, int>& A, const pair<string, int>& B) {
        //理解A代表根底元素，B代表新元素，这个操作的意思是比较之后，是不是需要弹出根底元素
        return (A.second > B.second || (A.second == B.second && A.first < B.first));
    }
};
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        priority_queue <pair<string, int>, vector<pair<string, int>>, Order > topkqueue{};
        unordered_map<string, int> frequence{};
        vector<string> res{};
        for (auto word : words)frequence[word]++;
        for (auto item : frequence) {
            if (topkqueue.size() < k) topkqueue.push(item);
            else {
                topkqueue.push(item);
                topkqueue.pop();
            }
        }
        while (topkqueue.size()) {
            res.push_back(topkqueue.top().first);
            topkqueue.pop();
        }
        reverse(res.begin(), res.end());
        return res;
    }
};

int main() {
    vector<string> inputstr{ "i", "love", "leetcode", "i", "love", "coding" };
    int k = 1;
    vector<string> topk = Solution().topKFrequent(inputstr, k);
    return 0;
}