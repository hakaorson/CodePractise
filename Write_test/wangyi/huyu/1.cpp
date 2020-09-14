// # nums = list(map(int, input().split()))
// # cars = sorted(nums, key=lambda x: x[0], reverse=True)

// # " ".join(map(str,nums))
// boxNum, personNum = list(map(int, input().split()))
// boxNum += 1
// boxValueList = list(map(int, input().split()))
// boxValueList.insert(0, 0)
// boxStatusList = [[]for i in range(boxNum)]
// for per in range(personNum):
//     actionNum = int(input())
//     personnalPrice = 0
//     leftHand = 0
//     rightHand = 0
//     bag = []
//     for actIndex in range(actionNum):
//         act = list(input().split())
//         if act[1] == 'keep':
//             if act[0] == 'left':
//                 bag.append(str(leftHand))
//                 leftHand = 0
//             else:
//                 bag.append(str(rightHand))
//                 rightHand = 0
//         elif act[1] == 'take':
//             target = int(act[2])
//             takeResult = target
//             if len(boxStatusList[target]):
//                 takeResult = boxStatusList[target].pop(-1)
//             if act[0] == 'left':
//                 leftHand = takeResult
//             else:
//                 rightHand = takeResult
//         else:
//             if act[0] == 'left':
//                 boxStatusList[int(act[2])].append(leftHand)
//                 leftHand = 0
//             else:
//                 boxStatusList[int(act[2])].append(rightHand)
//                 rightHand = 0
//     for item in bag:
//         personnalPrice += boxValueList[int(item)]
//     print(personnalPrice)
#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <unordered_map>
#include <array>
#include <numeric>
#include <stack>
#include <string>
using namespace std;


int main() {
    int boxNum, personNum;
    cin >> boxNum >> personNum;
    vector<int> boxValueList{ 0 };
    vector<stack<int>> boxStatus{ stack<int>{} };

    for (int i = 0; i < boxNum; i++) {
        int tmp;
        cin >> tmp;
        boxValueList.push_back(tmp);
        boxStatus.push_back(stack<int>{});
    }
    for (int i = 0; i < personNum; i++) {
        vector<int> bag{};
        int leftHand{}, rightHand{};
        int actNum{};
        cin >> actNum;
        for (int j = 0; j < actNum; j++) {
            string hand, act, target;
            cin >> hand >> act;
            if (act != "keep")
                cin >> target;
            if (act == "keep") {
                if (hand == "left") {
                    //atoi(target.c_str())
                    bag.push_back(leftHand);
                    leftHand = 0;
                }
                else {
                    bag.push_back(rightHand);
                    rightHand = 0;
                }
            }
            else if (act == "take") {
                int takeResult = stoi(target);
                if (!boxStatus[stoi(target)].empty()) {
                    takeResult = boxStatus[stoi(target)].top();
                    boxStatus[stoi(target)].pop();
                }
                if (hand == "left")
                    leftHand = takeResult;
                else
                    rightHand = takeResult;
            }
            else {
                if (hand == "left") {
                    boxStatus[stoi(target)].push(leftHand);
                    leftHand = 0;
                }
                else {
                    boxStatus[stoi(target)].push(rightHand);
                    rightHand = 0;
                }
            }
        }
        int result{};
        for (auto choose : bag) {
            result += boxValueList[choose];
        }
        if (leftHand!=0)
            result+= boxValueList[leftHand];
        if (rightHand!=0)
            result += boxValueList[rightHand];
        cout << result<<endl;
    }
    return 0;


}