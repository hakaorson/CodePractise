#include <iostream>
#include <string>
#include <stack>
using namespace std;

string func(string& st, int k) {
	stack<char> chstack{};
	stack<int> intstack{};
	for (auto ch: st) {
		if (chstack.empty() || chstack.top() != ch) {
			chstack.push(ch);
			intstack.push(1);
		}
		else {
			int temp = intstack.top();
			intstack.pop();
			temp++;
			if (temp == k) {
				chstack.pop();
			}
			else {
				intstack.push(temp);
			}
		}
	}
	string res;
	while (!intstack.empty()) {
		char ch = chstack.top();
		int num = intstack.top();
		chstack.pop();
		intstack.pop();
		for (int i = 0; i < num; i++) {
			res.insert(res.begin(), ch);
		}
	}
	return res;
}


int main()
{
	string st="abbcccbe";
	int k = 3;
	string result = func(st, k);

}