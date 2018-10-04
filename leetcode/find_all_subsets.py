# https://leetcode.com/problems/subsets/description/
# ITERATIVE APPROACH
class Solution:
    def subsets(self, nums):
        cur_state = [[]]
        for num in nums:
            new_states = []
            for state in cur_state:
                # print(state)
                first_new_state = state + [num]
                second_new_state = state
                new_states.append(first_new_state)
                new_states.append(second_new_state)
            cur_state = new_states
        return cur_state

# BIT OPERATION APPROACH
class Solution:
    def subsets(self, nums):
        results_size = 2 ** (len(nums))
        counter = 0
        j = 0
        result = []
        for counter in range(0, results_size):
            this_set = []
            for j in range(0, len(nums)):
                if ((counter & (1 << j)) > 0):
                    this_set.append(nums[j])
            result.append(this_set)
        return result

# RECURSIVE APPROACH
