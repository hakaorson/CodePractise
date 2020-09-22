#include <vector>
#include <deque>
#include <iostream>
#include <algorithm>
#include <array>
using namespace std;

const int maxsize = 10000;
char charmatrix[maxsize][maxsize]{};

void compute(char (&matrix)[maxsize][maxsize],int left,int low,int right,int up ) {
    int index = 0;
    while (true) {
        for (int i = left; i <= right; i++) {
            matrix[low][i] = (char)('A' + index++);
            index = index % 26;
        }
        if (++low > up)break;

        for (int i = low; i <= up; i++) {
            matrix[i][right] = (char)('A' + index++);
            index = index % 26;
        }
        if (--right < left)break;

        for (int i = right; i >= left; i--) {
            matrix[up][i] = (char)('A' + index++);
            index = index % 26;
        }
        if (--up < low)break;

        for (int i = up; i >= low; i--) {
            matrix[i][left] = (char)('A' + index++);
            index = index % 26;
        }
        if (++left > right)break;
    }
};


int main() {
    int m, n;
    cin >> m >> n;
    compute(charmatrix, 0, 0, n - 1, m - 1);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout << charmatrix[i][j] << ' ';
        }
        cout << endl;
    }
    return 0;
}