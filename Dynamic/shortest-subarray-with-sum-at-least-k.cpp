class Solution {
public:
    int shortestSubarray(vector<int>& A, int K) {
        A.insert(A.begin(), 0);
        vector<int>sums = { 0 };
        for (int i = 1; i < A.size(); i++)
            sums.push_back(sums.back() + A[i]);
        int res = A.size() + 1;
        deque<pair<int, int>> mydeque{ pair<int,int>(0,0) };
        for (int i = 1; i < A.size(); i++) {
            if (sums[i] <= mydeque.back().second) {
                while (mydeque.size() && sums[i] <= mydeque.back().second)
                    mydeque.pop_back();
            }
            else {
                while (mydeque.size() && sums[i] - mydeque.front().second >= K) {
                    res = min(res, i- mydeque.front().first);//需要修改
                    mydeque.pop_front();
                }
            }
            mydeque.push_back(pair<int, int>(i, sums[i]));
        }
        if (res == A.size() + 1)return -1;
        else return res;
    }
};
//关键是从后往前看，前缀和可能是一个波浪上升的曲线
//同一个和有不同的情况，但是对于后面的点来说，只有最近的和才是有意义的（因为有了最近的和，前面的和就没有意义了）