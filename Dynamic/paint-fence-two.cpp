#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <unordered_map>
#include <array>
#include <numeric>
using namespace std;

const int maxsize{ 100 };

int main() {
	int size{};
	cin >> size;
	int matrix[maxsize + 1]{};
	for (int i = 1; i <= size; i++) {
		if (i == 1) {
			matrix[i] = 3;continue;
		}
		else if (i == 2) {
			matrix[i] = 6; continue;
		}
		else {
			matrix[i] = matrix[i - 1];
			matrix[i] += matrix[i - 2] * 2;
		}
	}
	int result = matrix[size];
	cout << result;
}