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
    for (string::iterator itor = base.begin(); itor != base.end(); itor++)
        base_int.push_back(static_cast<int>(*itor));
    	sort(edges.begin(), edges.end(), [](tuple<int, int, int> A, tuple<int, int, int> B) {return get<2>(A) > get<2>(B); });
    return 0;
}