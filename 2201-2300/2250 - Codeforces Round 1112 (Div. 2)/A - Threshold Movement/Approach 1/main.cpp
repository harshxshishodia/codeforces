#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int testCases;
    cin >> testCases;

    while (testCases--) {
        int n;
        cin >> n;

        long long minimumOddPositionWeight = LLONG_MAX;
        long long maximumEvenPositionWeight = LLONG_MIN;

        for (int position = 1; position <= n; ++position) {
            long long weight;
            cin >> weight;

            if (position % 2 == 1) {
                minimumOddPositionWeight = min(minimumOddPositionWeight, weight);
            } else {
                maximumEvenPositionWeight = max(maximumEvenPositionWeight, weight);
            }
        }

        const bool hasPerfectThreshold =
            n % 2 == 0 &&
            maximumEvenPositionWeight + 1 < minimumOddPositionWeight;

        cout << (hasPerfectThreshold ? "YES" : "NO") << '\n';
    }

    return 0;
}
