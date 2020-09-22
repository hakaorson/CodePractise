#include <iostream>
#include <array>
#include <vector>
using namespace std;
int main()
{
    string base, block;
    base = "2102";
    block = "11";
    // cin >> base >> block;
    vector<int> base_int;
            vector<vector<vector<bool>>> visited(m, vector<vector<bool>>(n, vector<bool>(k + 1, false)));
    for (string::iterator itor = base.begin(); itor != base.end(); itor++)
        base_int.push_back(static_cast<int>(*itor));
    	sort(edges.begin(), edges.end(), [](tuple<int, int, int> A, tuple<int, int, int> B) {return get<2>(A) > get<2>(B); });
    return 0;
    '%.2f' % nums[0]
}

#include <vector>
#include <deque>
#include <iostream>
#include <algorithm>
#include <array>
using namespace std;

const int maxsize = 10000;
char charmatrix[maxsize][maxsize]{};

bool match(string a,string b) {
    a.insert(a.begin(), '&');
    b.insert(b.begin(), '&');
    int a_size = a.size();
    int b_size = b.size();
    vector<vector<bool>> dp{};
    for (int i = 0; i < a_size; i++) {
        vector<bool> temp{};
        for (int j = 0; j < b_size; j++) {
            temp.push_back(false);
        }
        dp.push_back(temp);
    }
    dp[0][0] = true;
    for (int i = 0; i < a_size; i++) {
        for (int j = 0; j < b_size; j++) {
        }
    }
    return 1;

};


int main() {
    string a, b;
    cin >> a >> b;
    if (match(a, b))cout << "true";
    else cout << "false";
    return 0;
}