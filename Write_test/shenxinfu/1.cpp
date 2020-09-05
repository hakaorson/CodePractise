#include <iostream>
#include <array>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    const long sizeN = 1000000;
    const long sizeHeight = 10000000;
    int n;
    array<long, sizeN> *nums = new array<long, sizeN>{};
    cin >> n;
    long minnum = INT16_MAX;
    long size = 0;
    long sumnum = 0;
    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
        minnum = min<long>(nums[i], minnum);
        sumnum = nums[i];
        size++;
    }
    cout << sumnum - minnum * size;
    return 0;
}