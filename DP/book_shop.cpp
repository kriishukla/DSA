#include <bits/stdc++.h>
using namespace std;
#define fast_io ios_base::sync_with_stdio(false); cin.tie(NULL);
#define fr(i, n) for(int i = 1; i <= n; i++)
#define ll long long

int main() {
    fast_io;
    ll t, n, x;
    t = 1;
    while (t--) {
        cin >> n >> x;
        vector<int> price(n + 1), pages(n + 1);
        fr(i, n)
            cin >> price[i];
        fr(i, n)
            cin >> pages[i];

        int dp[n + 1][x + 1];

        for (int i = 0; i <= n; i++) {
            for (int money = 0; money <= x; money++) {
                if (money == 0 || i == 0)
                    dp[i][money] = 0;
                else {
                    int op1 = (i == 1) ? 0 : dp[i - 1][money];
                    int op2 = (money < price[i]) ? 0 : pages[i] + dp[i - 1][money - price[i]];
                    dp[i][money] = max(op1, op2);
                }
            }
        }

        cout << dp[n][x];
    }
    return 0;
}
