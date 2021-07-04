// Given an array of integers, find two numbers such that they add up to a specific target number.

// The function twoSum should return indices of the two numbers such that they add up to the target,
// index1 must be less than index2. 
// Please note that your returned answers (both index1 and index2) are zero-based.

#include <cassert>
#include <iostream>
#include <vector>

class Solution {
public:
    /**
     * @param numbers: An array of Integer
     * @param target: target = numbers[index1] + numbers[index2]
     * @return: [index1, index2] (index1 < index2)
     */
    std::vector<int> twoSum(std::vector<int> &numbers, int target) {
        // write your code here
        std::vector<int> result;

        for (std::vector<int>::iterator first_num_it = numbers.begin(); first_num_it != numbers.end(); first_num_it++) {
            std::vector<int>::iterator second_num_it = std::find(first_num_it + 1, numbers.end(), target - *first_num_it);

            if (second_num_it != numbers.end()) {
                int first_index = std::distance(numbers.begin(), first_num_it);
                int second_index = std::distance(numbers. begin(), second_num_it);
                result.push_back(first_index);
                result.push_back(second_index);
                return result;
            }
        }

        return result;
    }
};

int main() {
    Solution s;
    // test 1
    std::vector<int> test_input_1;
    test_input_1.push_back(1);
    test_input_1.push_back(0);
    test_input_1.push_back(-1);

    std::vector<int> test_expected_output_1;
    test_expected_output_1.push_back(1);
    test_expected_output_1.push_back(2);

    std::vector<int> test_output_1;
    test_output_1 = s.twoSum(test_input_1, -1);
    assert(test_output_1 == test_expected_output_1);

    return 0;
}