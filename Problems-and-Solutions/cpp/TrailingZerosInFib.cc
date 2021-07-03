#include <iostream>

// Given an integer n, calculate the number of trailing zeros in n!.
// The time complexity of your algorithm should be O(logn)

class Solution {
public:
    /**
     * @param n: A long integer
     * @return: An integer, denote the number of trailing zeros in n!
     */
    long long trailingZeros(long long n) {
        // there will only be trailing zeros if there are multiples of 5 before the n
        int trailing_zeros = 0;
        while (n >= 5) {
            trailing_zeros++;
            n -= 5;
        }
        return trailing_zeros;
    }
};

int main() {
    Solution s;
    std::cout << s.trailingZeros(5) << std::endl;   // should return 1
    return 0;
}