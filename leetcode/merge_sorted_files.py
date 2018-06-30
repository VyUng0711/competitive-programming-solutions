import heapq


# Complexity O(n*logk), k is the number of sorted files.
def merge_sorted_files_1(sorted_files):
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

print (merge_sorted_files_1([[3, 5, 7], [0, 6], [0, 6, 28]]))
# Complexity O(n*logn)
def merge_sorted_files_2(sorted_files):
	my_list = []
	for file in sorted_files:
		for x in file:
			my_list.append(x)
	heapq.heapify(my_list)
	sorted_list = []
	length = len(my_list)
	for i in range(length):
		sorted_list.append(heapq.heappop(my_list))
	return sorted_list
#print (merge_sorted_files_2([[3, 5, 7], [0, 6], [0, 6, 28]]))
