// n = int(input())
// nums = list(map(int, input().split(' ')))
// max_num = nums[0]
// result = 0
// for num in nums:
//     if num < max_num:
//         result += 1
//     else:
//         max_num = num
// print(result)
#include <iostream>
#include <array>
#include <string>
#include <vector>
using namespace std;
int main()
{
    int n;
    cin>>n;
    vector<int> nums;
    for(int i=0;i<n;i++){
        int temp;
        cin>>temp;
        nums.push_back(temp);
    }
    int maxnum=nums[0];
    int reuslt=0;
    for(auto num:nums){
        if (num<maxnum){
            reuslt+=1;
        }else{
            maxnum=num;
        }
    }
    cout<<reuslt;
    return 0;
}