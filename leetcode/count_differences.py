# Time Complexity: O(n^2)
def count_difference_k(array, k):
	count = 0
	for i in range(len(array)):
		for j in range(len(array)):
			d = array[i] - array[j]
			if d == k:
				count += 1
	return count

# Time Complexity: O(n)
def optimized_count_difference_k(array, k):
	possible_results = {}
	count = 0
	for i in range(len(array)):
		if array[i] in possible_results:
			count += possible_results[array[i]]
		possible_results[array[i] + k] = possible_results.get(array[i] + k, 0) + 1
		possible_results[array[i] - k] = possible_results.get(array[i] - k, 0) + 1
	return count


print(optimized_count_difference_k([1, 7, 5, 9, 2, 12, 3], 2))
# Example: [1, 7, 5, 9, 2, 12, 3], k = 2
# 1: {-1, 3}
# 7: {-1, 3, 5, 9}
# 5: count = 1 {-1, 3, 5, 9, 7}  (7, 5)
# 9: count = 2 {-1, 3, 5, 9, 7, 11} (7, 9)
# 2: {-1, 3, 5, 9, 7, 11}
# 12: {-1, 3, 5, 9, 7, 10, 14}
# 3: count = 3 (3 5)
