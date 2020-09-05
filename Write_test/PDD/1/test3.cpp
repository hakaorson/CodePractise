
#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
const int MAX_N = 200025;
struct node
{
    int x,y;
    bool operator < (const node other)
    {
        return y < other.y;
    }
}arr[MAX_N];
struct tmpnode
{
    int x,y;
}brr[MAX_N];
int MINN[MAX_N];
int main()
{
    memset(MINN,0x3f,sizeof(MINN));
    int n,m,k,ans = -1;
    scanf("%d%d%d",&n,&m,&k);
    for(int i = 1;i<=n;++i)
    {
        scanf("%d%d",&arr[i].x,&arr[i].y);
        if(arr[i].y>=k)
        {
            if(ans==-1) ans = arr[i].x;
            else ans = min(ans,arr[i].x);
        }
    }
    for(int i = 1;i<=n;++i)
    {
        MINN[arr[i].y] = min(MINN[arr[i].y],arr[i].x);
    }
    for(int i = 100000;i>=0;--i)
    {
        MINN[i] = min(MINN[i+1],MINN[i]);
    }
    for(int i = 1;i<=m;++i)
    {
        scanf("%d%d",&brr[i].x,&brr[i].y);
        if(brr[i].y>=k)
        {
            if(ans==-1) ans = brr[i].x;
            else ans = min(ans,brr[i].x);
        }
    }
    for(int i = 1;i<=m;++i)
    {
        if(brr[i].y>=k) continue;
        else
        {
            if(ans == -1) ans = MINN[k-brr[i].y]+brr[i].x;
            else ans = min(ans,MINN[k-brr[i].y]+brr[i].x);
        }
    }
    if(k==0)
    {
        printf("0\n");
        return 0;
    }
    if(ans>=200000)
    {
        printf("-1\n");
        return 0;
    }
    printf("%d\n",ans);
    return 0;
}