#include <iostream>
#include <vector>

using namespace std;

int extractMaxDigit(int number) {
    int maxDigit = 0;

    // Convert the number to a string for easier iteration over its digits
    string numberStr = to_string(number);

    // Iterate over each digit in the number
    for (char digit : numberStr) {
        int digitVal = digit - '0';  // Convert the digit back to integer for comparison
        if (digitVal > maxDigit) {
            maxDigit = digitVal;
        }
    }

    return maxDigit;
}

int main() {
    int n;
    cin >> n;

    vector<int> arr(n + 1, 0);

    for (int i = 0; i < 10; i++) {
        if (n >= i) {
            arr[i] = 1;
        }
    }

    if (n >= 10) {
        for (int i = 10; i <= n; i++) {
            int k = i - extractMaxDigit(i);
            arr[i] = (1 + arr[k]) % (int(1e9) + 7);
        }
    }

    cout << arr[n] % (int(1e9) + 7) << endl;

    return 0;
}
