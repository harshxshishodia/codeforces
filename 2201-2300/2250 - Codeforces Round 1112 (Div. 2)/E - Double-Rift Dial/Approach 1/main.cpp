#include <bits/stdc++.h>
using namespace std;

class MaximumSegmentTree {
public:
    explicit MaximumSegmentTree(int size)
        : size_(size), maximum_(4 * size + 4), lazy_(4 * size + 4) {}

    void add(int left, int right, int value) {
        if (left <= right) {
            add(1, 1, size_, left, right, value);
        }
    }

    int maximum() const {
        return maximum_[1];
    }

    int firstAbove(int limit) {
        return firstAbove(1, 1, size_, limit);
    }

    void remove(int position) {
        remove(1, 1, size_, position);
    }

private:
    static constexpr int REMOVED = -1'000'000'000;

    int size_;
    vector<int> maximum_;
    vector<int> lazy_;

    void apply(int node, int value) {
        maximum_[node] += value;
        lazy_[node] += value;
    }

    void push(int node) {
        if (lazy_[node] == 0) {
            return;
        }
        apply(node * 2, lazy_[node]);
        apply(node * 2 + 1, lazy_[node]);
        lazy_[node] = 0;
    }

    void pull(int node) {
        maximum_[node] = max(maximum_[node * 2], maximum_[node * 2 + 1]);
    }

    void add(
        int node,
        int segmentLeft,
        int segmentRight,
        int queryLeft,
        int queryRight,
        int value
    ) {
        if (queryLeft <= segmentLeft && segmentRight <= queryRight) {
            apply(node, value);
            return;
        }

        push(node);
        const int middle = (segmentLeft + segmentRight) / 2;
        if (queryLeft <= middle) {
            add(node * 2, segmentLeft, middle, queryLeft, queryRight, value);
        }
        if (queryRight > middle) {
            add(
                node * 2 + 1,
                middle + 1,
                segmentRight,
                queryLeft,
                queryRight,
                value
            );
        }
        pull(node);
    }

    int firstAbove(int node, int segmentLeft, int segmentRight, int limit) {
        if (segmentLeft == segmentRight) {
            return segmentLeft;
        }

        push(node);
        const int middle = (segmentLeft + segmentRight) / 2;
        if (maximum_[node * 2] > limit) {
            return firstAbove(node * 2, segmentLeft, middle, limit);
        }
        return firstAbove(node * 2 + 1, middle + 1, segmentRight, limit);
    }

    void remove(int node, int segmentLeft, int segmentRight, int position) {
        if (segmentLeft == segmentRight) {
            maximum_[node] = REMOVED;
            lazy_[node] = 0;
            return;
        }

        push(node);
        const int middle = (segmentLeft + segmentRight) / 2;
        if (position <= middle) {
            remove(node * 2, segmentLeft, middle, position);
        } else {
            remove(node * 2 + 1, middle + 1, segmentRight, position);
        }
        pull(node);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int testCases;
    cin >> testCases;

    while (testCases--) {
        int n;
        cin >> n;

        vector<int> permutation(n);
        for (int& value : permutation) {
            cin >> value;
        }

        MaximumSegmentTree blockCounts(n);
        vector<int> lastPosition(n + 2);
        int answer = n;

        for (int right = 1; right < 2 * n; ++right) {
            const int leftBoundary = max(1, right - n + 1);
            const int rightBoundary = min(right, n);
            const int value = permutation[(right - 1) % n];

            blockCounts.add(leftBoundary, rightBoundary, 1);

            if (
                value > 1 &&
                lastPosition[value - 1] >= leftBoundary
            ) {
                blockCounts.add(
                    leftBoundary,
                    min(rightBoundary, lastPosition[value - 1]),
                    -1
                );
            }

            if (
                value < n &&
                lastPosition[value + 1] >= leftBoundary
            ) {
                blockCounts.add(
                    leftBoundary,
                    min(rightBoundary, lastPosition[value + 1]),
                    -1
                );
            }

            lastPosition[value] = right;

            while (blockCounts.maximum() > 2) {
                const int invalidStart = blockCounts.firstAbove(2);
                blockCounts.remove(invalidStart);
                --answer;
            }
        }

        cout << answer << '\n';
    }

    return 0;
}
