
#include <vector>
using namespace std;
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution
{
public:
    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        vector<ListNode>::iterator itor;
    }
    ListNode *initList(vector<int> &ints)
    {
    }
};
int main()
{
    Solution solu = Solution();
    vector<ListNode *> vec;
    vector<int> ints0 = {1, 2, 3};
    vec.push_back(solu.initList(ints0));
    solu.mergeKLists(vec);
}
