/*
1
4 4
....
....
....
....
3 3
.o.
/|\
./\
0 0 1 1
*/
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
const int maxsize = 100;

class TV {
public:
    int tvsizeX, tvsizeY, graphsizeX, graphsizeY;
    vector<vector<char>> tvmatrix;
    vector<vector<char>> graphmatrix;
    vector<vector<char>> beforematrix;
    vector<vector<char>> nextmatrix;
    int beginX, beginY, skipX, skipY;
    
};


void clean(array<array<char, maxsize>, maxsize>* pre, array<array<char, maxsize>, maxsize>* screen, int left, int right, int up, int down)
{
    for (int i = up; i < down; i++)
        for (int j = left; j < right; j++)
            (*pre)[i][j] = (*screen)[i][j];
}
void fusion(array<array<char, maxsize>, maxsize>* screen,
    array<array<char, maxsize>, maxsize>* people,
    array<array<char, maxsize>, maxsize>* now,
    int left, int right, int up, int down,
    int beginn, int beginm, int peopleN, int peopleM)
{
    for (int i = up; i < down; i++)
        for (int j = left; j < right; j++)
        {
            if (i - beginn >= 0 && j - beginm >= 0 && i - beginn < peopleN && j - beginm < peopleM)
            {
                (*now)[i][j] = (*people)[i - beginn][j - beginm];
            }
            else
            {
                (*now)[i][j] = (*screen)[i][j];
            }
        }
}
int compare(array<array<char, maxsize>, maxsize>* pre,
    array<array<char, maxsize>, maxsize>* now,
    int left, int right, int up, int down)
{
    int result = 0;
    for (int i = up; i < down; i++)
        for (int j = left; j < right; j++)
        {
            if ((*now)[i][j] == (*pre)[i][j])
            {
                result += 1;
            }
        }
    return result;
}

int main()
{
    int N{};
    char temp;
    cin >> N;
    for (int n = 0; n < N; n++)
    {
        TV tv{};
        cin >> tv.tvsizeX >> tv.tvsizeY;
        for (int i = 0; screenn < screenN; screenn++)
            for (int screenm = 0; screenm < screenM; screenm++)
            {
                cin >> temp;
                (*screen)[screenn][screenm] = temp;
            }
        int peopleN, peopleM;
        cin >> peopleN >> peopleM;
        for (int peoplen = 0; peoplen < peopleN; peoplen++)
            for (int peoplem = 0; peoplem < peopleM; peoplem++)
            {
                cin >> temp;
                (*people)[peoplen][peoplem] = temp;
            }

        int beginn, beginm, skipn, skipm;
        cin >> beginn >> beginm >> skipn >> skipm;
        int result = 0;
        while (true)
        {
            int left, right, up, down;
            left = max(0, min(beginm, beginm + skipm));
            up = max(0, min(beginn, beginn + skipn));
            right = min(screenM, max(beginm + peopleM, beginm + peopleM + skipm));
            down = min(screenN, max(beginn + peopleN, beginn + peopleN + skipn));
            clean(now, screen, left, right, up, down);
            clean(pre, screen, left, right, up, down);
            fusion(screen, people, pre, left, right, up, down, beginn, beginm, peopleN, peopleM);
            fusion(screen, people, now, left, right, up, down, beginn + skipn, beginm + skipm, peopleN, peopleM);
            beginn += skipn;
            beginm += skipm;
            result += compare(now, pre, left, right, up, down);
        }

        cout << result << endl;

        delete screen, people, pre, now;
    }
}