#include <iostream>
#include <array>
using namespace std;

int main()
{
    int n, l, r;
    cin >> n >> l, r;
    array<int, 3> statics;
    for (int i = l; i <= r; i++)
        statics[i % 3] ++;
    return 0;
}