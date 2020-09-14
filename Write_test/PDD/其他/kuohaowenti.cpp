#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <unordered_map>
#include <array>
#include <numeric>
#include <stack>
using namespace std;


int main() {
	string input{};
	cin >> input;
	stack<char> kuohao{};
	stack<int> result{};
	for (auto ch : input) {
		if (ch == '(') {
			kuohao.push(ch);
			result.push(0);
		}
		else {
			if (result.top() == 0) {
				result.pop();
				result.push(1);
				kuohao.pop();
			}
			else {
				int temp = 0;
				while (result.top() != 0) {
					temp += result.top();
					result.pop();
				}
				result.pop();
				result.push(temp*temp);
				kuohao.pop();
			}
		}
	}
	cout << result.top();
}