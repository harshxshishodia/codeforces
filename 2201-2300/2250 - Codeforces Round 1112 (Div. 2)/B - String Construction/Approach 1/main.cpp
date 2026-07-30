#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int testCases;
    cin >> testCases;

    while (testCases--) {
        int n;
        int equalPairs;
        cin >> n >> equalPairs;

        const int blockCount = n - equalPairs;
        if (blockCount == 1) {
            cout << -1 << '\n';
            continue;
        }

        const int zeroCount = (n + 1) / 2;
        const int oneCount = n / 2;
        const int zeroBlocks = (blockCount + 1) / 2;
        const int oneBlocks = blockCount / 2;

        vector<int> blockLengths(blockCount, 1);
        blockLengths[0] += zeroCount - zeroBlocks;
        blockLengths[1] += oneCount - oneBlocks;

        string answer;
        answer.reserve(n);
        for (int block = 0; block < blockCount; ++block) {
            answer.append(blockLengths[block], block % 2 == 0 ? '0' : '1');
        }

        cout << answer << '\n';
    }

    return 0;
}
