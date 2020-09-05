#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <unordered_map>
#include <array>
#include <numeric>
using namespace std;
/*
9 14
1 2 4
2 3 8
3 4 7
4 5 9
5 6 10
6 7 2
7 8 1
8 9 7
2 8 11
3 9 2
7 9 6
3 6 4
4 6 14
1 8 8
*/
//37

int findroot(int index, vector<int>& root) {
	int fathre = root[index];
	while (fathre != -1) {
		index = fathre;
		fathre = root[fathre];
	}
	return index;
}

int main() {
	int graphsize, edgenum;
	cin >> graphsize >> edgenum;
	vector<tuple<int, int, int>> edges{};
	vector<int> root{}, size{};
	for (int i = 0; i <= graphsize; i++) {
		root.push_back(-1);
		size.push_back(0);
	}
	for (int i = 0; i < edgenum; i++) {
		int v0, v1, weight;
		cin >> v0 >> v1 >> weight;
		edges.push_back(tuple<int, int, int>(v0, v1, weight));
	}
	sort(edges.begin(), edges.end(), [](tuple<int, int, int> A, tuple<int, int, int> B) {return get<2>(A) < get<2>(B); });
	for (auto cur : edges) {
		int v0 = get<0>(cur), v1 = get<1>(cur), weight = get<2>(cur);
		int v0RootIndex = findroot(v0, root), v1RootIndex = findroot(v1, root);
		if (v0RootIndex != v1RootIndex) {
			root[v0RootIndex] = v1RootIndex;
			size[v1RootIndex] += size[v0RootIndex] + weight;
			size[v0RootIndex] = 0;
		}
	}
	int result = accumulate(size.begin(), size.end(), 0);
	return 0;
}