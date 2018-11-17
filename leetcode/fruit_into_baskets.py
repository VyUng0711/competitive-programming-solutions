class Solution:
    def totalFruit(self, tree):
        max_count = 0
        i = 0
        j = 0
        baskets = {}
        while j < len(tree):
            while j < len(tree) and ((len(baskets) == 2 and tree[j] in baskets) or len(baskets) < 2):
                baskets[tree[j]] = baskets.get(tree[j], 0) + 1
                j += 1
            max_count = max(max_count, j - i)
            baskets[tree[i]] -= 1
            if baskets[tree[i]] == 0:
                del baskets[tree[i]]
            i += 1
        return max_count


