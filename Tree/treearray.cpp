
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


class ArrayTree {
public:
    ArrayTree(vector<int>& inputnums) :nums(inputnums),oldnums(inputnums),size(inputnums.size()) {
        nums.insert(nums.begin(), 0);
        oldnums.insert(oldnums.begin(), 0);
        size++;
        init();
    };
    int getright(int num) {
        return (num & (-num));
    }
    int getfather(int num) {
        int rightnum = getright(num);
        return (rightnum + num);
    }
    vector<int> getchilds(int num) {
        vector<int> result{};
        int rightnum = getright(num)-1;
        int oldnum = num - getright(num);
        while (rightnum > 0) {
            result.push_back(rightnum+oldnum);
            rightnum = rightnum - getright(rightnum);
        }
        return result;
    }
    void update(int index, int num) {
        int oldnum = oldnums[index];
        oldnums[index] = num;
        int subnum = num - oldnum;
        while (index < size) {
            nums[index] += subnum;
            index = getfather(index);
        }

    }
    int sumbefore(int i) {
        int res = 0;
        while (i) {
            res += nums[i];
            i -= getright(i);
        }
        return res;
    }
    int sumbetween(int i, int j) {
        return (sumbefore(j) - sumbefore(i - 1));
    }
private:
    vector<int> nums;
    int size;
    vector<int> oldnums;
    void init() {
        for (int i = 1; i < size; i++) {
            vector<int> children = getchilds(i);
            for (auto ch : children)
                nums[i] += nums[ch];
        }
    };
};


class NumArray {
public:
    NumArray(vector<int>& inputnums) :nums(inputnums), arraytree(inputnums), size(inputnums.size()) {
        nums.insert(nums.begin(), 0);
        size++;
    }//915630319

    void update(int i, int val) {
        arraytree.update(i + 1, val);
    }


    int sumRange(int i, int j) {
        return arraytree.sumbetween(i + 1, j + 1);
    }
private:
    vector<int> nums;
    ArrayTree arraytree;
    int size;
};


int main() {
    vector<int> nums{ 7,2,7,2,0 };
    NumArray* obj = new NumArray(nums);
    obj->update(4, 6);
    obj->update(0, 2);
    obj->update(0, 9);
    obj->update(3, 8);
    int param_2 = obj->sumRange(0, 4);
    return 0;
}
/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(i,val);
 * int param_2 = obj->sumRange(i,j);
 */