#include <iostream>
using namespace std;
int main()
{
    long n;
    cin >> n;
    int ans = 0;
    while (n > 0)
    {
        ans += n & 1;
        n >>= 1;
    }
    cout << ans;
    return 0;
}
