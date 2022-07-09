/*
First and foremost, it can be proven that (a⊕b)+(b⊕c)+(a⊕c) is always even, 
for all possible non-negative values of a, b and c


Therefore, if n
is even, one possible solution is a=0, b=0 and c=n2. In this case, (a⊕b)+(b⊕c)+(a⊕c)=0+n2+n2=n

. Otherwise, there are no solutions.

Time complexity per testcase: O(1)

*/
#include <bits/stdc++.h>
using namespace std;
#define mp             make_pair
#define pb             push_back
#define fi             first
#define se             second
#define sz(x)          (int)((x).size())
#define fill(x, y)     memset(x, y, sizeof(y))
#define all(x)         (x).begin(), (x).end()
#define sci(x)         int x;       scanf("%d", &x);
#define scii(x, y)     int x, y;    scanf("%d %d", &x, &y);
#define sciii(x, y, z) int x, y, z; scanf("%d %d %d", &x, &y, &z);
#define TC(x)          sci(x); while(x --)
#define eprintf(...)   fprintf(stderr, __VA_ARGS__)
#define debug(x)       { cerr << #x << " = " << x << endl; }
#define rep(i, x, y)   for (__typeof(x) i = x; i <= y; i ++)
#define repi(i, x, y)  for (__typeof(x) i = x; i >= y; i --)
#define fore(itr, x)   for (__typeof(x.begin()) itr = x.begin(); itr != x.end(); itr ++)
#define forei(itr, x)  for (__typeof(x.end()) itr = x.end() - 1; itr != x.begin() - 1; itr --)
typedef long long      ll;
typedef pair<int, int> ii;
typedef pair<ii, int>  iii;
typedef vector<int>    vi;
typedef vector<ii>     vii;
typedef vector<iii>    viii;
const   int            inf = 0;
const   double         eps = 0;
const   int            ms  = 0;
const   int            md  = 0;


void solve()
{
int n;
    cin>>n;

    if(n%2==0)
        cout<<"0 0 "<<n/2<<'\n';
    else
        cout<<"-1\n";
}

int main() {
    ios::sync_with_stdio(false);

    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
}
 