import heapq 

def merge_sorted_arrays(sorted_files):
	min_heap = []
	sorted_array_iters = [iter(x) for x in sorted_files]
	for i, it in enumerate(sorted_array_iters):
		first_element = next(it, None)
		if first_element is not None:
			heapq.heappush(min_heap, (first_element, i))
	result = []
	while min_heap:
		smallest_entry, smallest_array_i = heapq.heappop(min_heap)
		smallest_array_iter = sorted_array_iters[smallest_array_i]
		result.append(smallest_entry)
		next_element = next(smallest_array_iter, None)
		if next_element is not None:
			heapq.heappush(min_heap, (next_element, smallest_array_i))
	return result

def sort_k_increasing_decreasing_array(a):
	start = 0
	increasing = True
	sorted_subarrays = []
	for i in range(1, len(a) + 1):
		if i == len(a) or (a[i - 1] >= a[i] and increasing == True) or (a[i - 1] < a[i] and increasing == False):
			if increasing == True:
				sorted_subarrays.append(a[start:i])
				increasing = False
			else:
				sorted_subarrays.append(a[i - 1:start - 1:-1])
				increasing = True
			start = i
	return merge_sorted_arrays(sorted_subarrays)

print (sort_k_increasing_decreasing_array([57, 131, 493, 294, 221, 339, 418, 452, 442, 190]))
