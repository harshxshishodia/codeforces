#include <bits/stdc++.h>
using namespace std;

namespace {
constexpr long long MOD = 998244353;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int testCases;
    cin >> testCases;

    while (testCases--) {
        int n;
        cin >> n;

        vector<int> frequency(n + 1);
        vector<char> seenBlock(n + 1, false);

        bool validShape = true;
        bool decreasing = false;
        int previousValue = -1;

        for (int index = 0; index < n - 1; ++index) {
            int value;
            cin >> value;
            ++frequency[value];

            if (value == n) {
                validShape = false;
            }

            if (value == previousValue) {
                continue;
            }

            if (seenBlock[value]) {
                validShape = false;
            }
            seenBlock[value] = true;

            if (previousValue != -1) {
                if (!decreasing && value < previousValue) {
                    decreasing = true;
                } else if (decreasing && value > previousValue) {
                    validShape = false;
                }
            }

            previousValue = value;
        }

        long long ways = 1;
        int usedValues = 0;

        for (int value = 1; value < n && ways != 0; ++value) {
            const int count = frequency[value];
            if (count == 0) {
                continue;
            }

            ++usedValues;
            for (int occurrence = 1; occurrence < count; ++occurrence) {
                const int choices = value - usedValues;
                if (choices <= 0) {
                    ways = 0;
                    break;
                }
                ways = ways * choices % MOD;
                ++usedValues;
            }
        }

        const long long answer = validShape ? 2 * ways % MOD : 0;
        cout << answer << '\n';
    }

    return 0;
}
