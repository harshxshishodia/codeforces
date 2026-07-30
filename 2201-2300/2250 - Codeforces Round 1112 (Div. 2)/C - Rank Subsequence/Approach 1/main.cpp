#include <bits/stdc++.h>
using namespace std;

struct ForbiddenRanks {
    int leftStart;
    int leftEnd;
    int rightStart;
    int rightEnd;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int testCases;
    cin >> testCases;

    while (testCases--) {
        int n;
        cin >> n;

        vector<ForbiddenRanks> elements(n);
        for (ForbiddenRanks& element : elements) {
            cin >> element.leftStart >> element.leftEnd;
            cin >> element.rightStart >> element.rightEnd;
        }

        int answer = 0;
        for (int length = n; length >= 1; --length) {
            int nextPosition = 1;

            for (const ForbiddenRanks& element : elements) {
                if (nextPosition > length) {
                    break;
                }

                const int rightRank = length - nextPosition + 1;
                const bool leftRankAllowed =
                    nextPosition < element.leftStart ||
                    nextPosition > element.leftEnd;
                const bool rightRankAllowed =
                    rightRank < element.rightStart ||
                    rightRank > element.rightEnd;

                if (leftRankAllowed && rightRankAllowed) {
                    ++nextPosition;
                }
            }

            if (nextPosition == length + 1) {
                answer = length;
                break;
            }
        }

        cout << answer << '\n';
    }

    return 0;
}
