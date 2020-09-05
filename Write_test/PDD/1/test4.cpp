
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <stack>
#include <queue>
using namespace std;
/*
#*****
#*****
******
******
******
******
*/
const int mod = 1000000009;
int f[2][7 * 7 * 7 * 7 * 7 * 7];
int pow7[15];
char w[15][15];
int main()
{
    pow7[0] = 1;
    for (int i = 1; i < 15; i++)
    {
        pow7[i] = pow7[i - 1] * 7;
    }
    for (int i = 0; i < 6; i++)
    {
        scanf("%s", w[i]);
    }
    int now = 0;
    f[now][0] = 1;
    for (int i = 0; i < 6; i++)
    {
        for (int j = 0; j < 6; j++)
        {
            now ^= 1;
            for (int k = 0; k < 7 * 7 * 7 * 7 * 7 * 7; k++)
            {
                f[now][k] = 0;
                if (j == 0 || k / pow7[j] % 7 != k / pow7[j - 1] % 7 || k / pow7[j] % 7 == k / pow7[j - 1] % 7 && k / pow7[j] % 7 == 0)
                {
                    if (w[i][j] == '#' && k / pow7[j] % 7 != 0)
                    {
                        for (int l = 0; l < 7; l++)
                        {
                            if (l != k / pow7[j] % 7)
                            {
                                f[now][k] = (f[now][k] + f[now ^ 1][k / pow7[j + 1] * pow7[j + 1] + l * pow7[j] + k % pow7[j]]) % mod;
                            }
                        }
                    }
                    else if (w[i][j] != '#' && k / pow7[j] % 7 == 0)
                    {
                        for (int l = 0; l < 7; l++)
                        {
                            f[now][k] = (f[now][k] + f[now ^ 1][k / pow7[j + 1] * pow7[j + 1] + l * pow7[j] + k % pow7[j]]) % mod;
                        }
                    }
                }
            }
        }
    }
    int ans = 0;
    for (int k = 0; k < 7 * 7 * 7 * 7 * 7 * 7; k++)
    {
        ans = (ans + f[now][k]) % mod;
    }
    cout << ans;
    return 0;
}