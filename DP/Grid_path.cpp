#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<vector<char>> arr1(n, vector<char>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr1[i][j];
        }
    }

    const int MOD = 1e9 + 7; // Define the modulo constant

    if (arr1[0][0] == '*' || arr1[n - 1][n - 1] == '*') {
        cout << 0 << endl;
    } else {
        vector<vector<long long>> arr2(n, vector<long long>(n, 0));

        if (arr1[0][0] == '.') {
            arr2[0][0] = 1;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (arr1[i][j] == '*') {
                    arr2[i][j] = 0;
                } else {
                    if (i > 0) {
                        arr2[i][j] += arr2[i - 1][j];
                        arr2[i][j] %= MOD; // Apply modulo here
                    }
                    if (j > 0) {
                        arr2[i][j] += arr2[i][j - 1];
                        arr2[i][j] %= MOD; // Apply modulo here
                    }
                }
            }
        }

        cout << arr2[n - 1][n - 1] % MOD << endl; // Apply modulo here for the final answer
    }

    return 0;
}
