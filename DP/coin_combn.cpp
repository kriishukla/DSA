#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    const int mod = 1000000007;
    vector<long long> dp(k + 1, 0);
    dp[0] = 1;

    for (int i = 1; i <= k; ++i) {
        for (int j = 0; j < n; ++j) {
            if (i - arr[j] >= 0) {
                dp[i] += dp[i - arr[j]];
                dp[i] %= mod;
            }
        }
    }

    cout << dp[k] << endl;

    return 0;
}
