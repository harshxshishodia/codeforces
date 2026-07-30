#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int testCases;
    cin >> testCases;

    while (testCases--) {
        int n;
        int targetXor;
        cin >> n >> targetXor;

        const bool isPowerOfTwo = (n & (n - 1)) == 0;
        if (!isPowerOfTwo || (n == 2 && targetXor != 0)) {
            cout << -1 << '\n';
            continue;
        }

        if (targetXor == 0) {
            for (int row = 0; row < n; ++row) {
                for (int column = 0; column < n; ++column) {
                    if (column > 0) {
                        cout << ' ';
                    }
                    cout << (row ^ column);
                }
                cout << '\n';
            }
            continue;
        }

        vector<char> visited(n, false);
        vector<int> evenPositionValues;
        vector<int> oddPositionValues;
        evenPositionValues.reserve(n / 2);
        oddPositionValues.reserve(n / 2);

        int pairIndex = 0;
        for (int value = 0; value < n; ++value) {
            if (visited[value]) {
                continue;
            }

            const int partner = value ^ targetXor;
            visited[value] = true;
            visited[partner] = true;

            vector<int>& destination =
                pairIndex < n / 4 ? oddPositionValues : evenPositionValues;
            destination.push_back(value);
            destination.push_back(partner);
            ++pairIndex;
        }

        vector<int> ordering(n);
        int evenIndex = 0;
        int oddIndex = 0;
        for (int index = 0; index < n; ++index) {
            if (index % 2 == 0) {
                ordering[index] = evenPositionValues[evenIndex++];
            } else {
                ordering[index] = oddPositionValues[oddIndex++];
            }
        }

        for (int row = 0; row < n; ++row) {
            for (int column = 0; column < n; ++column) {
                int value = ordering[row] ^ ordering[column];
                if (row % 2 == 1 && column % 2 == 1) {
                    value ^= targetXor;
                }

                if (column > 0) {
                    cout << ' ';
                }
                cout << value;
            }
            cout << '\n';
        }
    }

    return 0;
}
