#include <iostream>
#include <array>
#include <string>
#include <vector>
using namespace std;
int main()
{
    string a, b;
    cin >> a >> b;
    int result = 0;
    int len = a.size();
    for (int i = 0; i < len; i++)
    {
        if (a[i] == b[i])
        {
            result += 20;
        }
        else
        {
            if (result > 0)
            {
                result -= 10;
            }
        }
    }
    cout<<result;
    return 0;
}