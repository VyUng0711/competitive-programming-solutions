def trapping_rain_water(height):
  max_from_left = [0] * len(height)
  max_from_right = [0] * len(height)
  
  max_from_left[0] = height[0]
  for i in range(1, len(height)):
    max_from_left[i] = max(height[i], max_from_left[i - 1])
  
  max_from_right[len(height) - 1] = height[len(height) - 1]
  for j in range(len(height) - 2, -1, -1):
    max_from_right[j] = max(height[j], max_from_right[j + 1])
      
      
  trapped_water = 0
  for k in range(0, len(height)):
    trapped_water += max(min(max_from_left[k], max_from_right[k]) - height[k],0)
  print(max_from_left)
  print(max_from_right)
  return(trapped_water)

  
def trapping_rain_water_1(height):
  max_from_left = [0] * len(height)
  max_from_right = [0] * len(height)
  
  max_so_far_from_left = 0
  for i in range(len(height)):
    max_from_left[i] = max_so_far_from_left
    if height[i] > max_so_far_from_left:
      max_so_far_from_left = height[i]
      
  max_so_far_from_right = 0
  for j in range(len(height) - 1, -1, -1):
    max_from_right[j] = max_so_far_from_right
    if height[j] > max_so_far_from_right:
      max_so_far_from_right = height[j]
      
      
  trapped_water = 0
  for k in range(0, len(height)):
    trapped_water += max(min(max_from_left[k], max_from_right[k]) - height[k],0)
  print(max_from_left)
  print(max_from_right)
  return(trapped_water)

print(trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))
 