#include <vector>
#include <deque>
#include <iostream>
#include <algorithm>
#include <array>
using namespace std;


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
    for (int i = 1; i < a_size; i++) {
        for (int j = 1; j < b_size; j++) {
            if (a[i] == b[j] || b[j] == '.')dp[i][j] = dp[i - 1][j - 1];
            else if (b[j] == '*') {
                if (a[i] == b[j - 1] || b[j - 1] == '.') {
                    dp[i][j] = dp[i][j - 2] || dp[i - 1][j - 2] || dp[i - 1][j];
                }
                else dp[i][j] = dp[i][j - 2];
            }
            else if (b[j] == '+') {
                if (a[i] == b[j - 1] || b[j - 1] == '.') {
                    dp[i][j] = dp[i - 1][j - 2] || dp[i - 1][j];
                }
                else dp[i][j] = false;
            }
            else dp[i][j] = false;
        }
    }
    return dp[a_size-1][b_size-1];

};


int main() {
    string a, b;
    cin >> a >> b;
    if (match(a, b))cout << "true";
    else cout << "false";
    return 0;
}