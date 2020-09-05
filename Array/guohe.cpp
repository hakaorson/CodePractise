#include <iostream>
#include <thread>
#include <array>
#include <mutex>
#include <vector>
#include <atomic>
#include <algorithm>
#include <numeric>
using namespace std;
const int maxsize = 1000;
int result = 0;

void run(array<int, maxsize>& nums, int size) {
	if (size == 0);
	else if (size == 1) {
		result += nums[0];
	}
	else if (size == 2)
		result += nums[1];
	else if (size == 3)
		result += accumulate(nums.begin(), nums.end(), 0);
	else {
		result += min(2 * nums[0] + nums[size - 1] + nums[size - 2], nums[0] + 2 * nums[1] + nums[size - 1]);
		run(nums, size - 2);
	};
	return;
};

int main() {

	int n;
	cin >> n;
	array<int, maxsize> nums{};
	for (int i = 0; i < n; i++)
		cin >> nums[i];
	run(nums, n);
	return 0;
}

// 4
// 1 2 5 10