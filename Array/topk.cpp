#include <iostream>
#include <array>
using namespace std;
//基于堆排序的topk
void sort(array<int,10>& nums,int left,int right,int k){
    if (((right-left)==k) || (right==left)){
        return;
    }
    int refer=nums[left];
    int leftbound=left;
    for(int i=left+1;i<right;i++){
        if (nums[i]<refer){
            nums[leftbound]=nums[i];
            nums[i]=nums[leftbound+1];
            leftbound+=1;
        }else{
            continue;
        }
    }
    nums[leftbound]=refer;
    if (right-leftbound==k){
        return;
    }else if(right-leftbound>k){
        sort(nums, leftbound, right, k);
    }else{
        sort(nums, left, leftbound-1, k-(right-leftbound));
    }
    return;
}
int main() {
    array<int,10> nums={4,3,6,2,8,1,0,5,2,10};
    sort(nums,0,10,7);
    for(int i=3;i<10;i++){
        cout<<nums[i]<<endl;
    }
    //int a;
    //cin >> a;
    cout << "Hello World!" << endl;
}

