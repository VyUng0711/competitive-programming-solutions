def k_largest(max_heap, k):
  candidates = []
  candidates.append((max_heap[0], 0))
  result = []
  for i in range(k):
    
    candidate_idx = candidates[0][1]
    result.append(heapq.heappop(candidates)[0])
    
    left_child_idx = 2 * candidate_idx + 1
    if left_child_idx < len(max_heap):
      heapq.heappush(candidates, (max_heap[left_child_idx], left_child_idx))
      
    right_child_idx = 2 * candidate_idx + 2
    if right_child_idx < len(max_heap):
      heapq.heappush(candidates, (max_heap[right_child_idx], right_child_idx))
      
  return result

print (k_largest([-561, -314, -401, -28, -156, -359, -271, -11, -3], 4))