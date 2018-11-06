# https://www.coderbyte.com/results/vyung:Scale%20Balancing:Python

def ScaleBalancing(strArr): 
    two_sides = list(map(int, strArr[0][1: -1].split(', ')))
    scale_list = list(map(int, strArr[1][1:-1].split(', '))) 

    diff = abs(two_sides[0] - two_sides[1])
#     two_sides = eval(strArr[0])
#     scale_list = eval(strArr[1])
    
    seen = set()
    list_result = []
    
    for a in scale_list:
      
      if a == diff:
        list_result.append([a])
        # return str(a)

      if a - diff in seen:
#         result = sorted([a, a - diff])
#         return ','.join([x for x in result])
        list_result.append(sorted([a, a - diff]))
        # return '{},{}'.format(*sorted([a, a - diff]))

      if a + diff in seen:
        list_result.append(sorted([a, a + diff]))
        # return '{},{}'.format(*sorted([a, a + diff]))
      
      if diff - a in seen:
        list_result.append(sorted([a, diff - a]))
        # return '{},{}'.format(*sorted([a, diff - a])) 
      
      seen.add(a)
      
    if not list_result:
      return "not possible"
    else:
      sorted_result = sorted(list_result, key= lambda x: sum(x))
      if len(sorted_result[0]) == 1:
        return '{}'.format(*sorted_result[0])
      else:
        return '{},{}'.format(*sorted_result[0])


# Sort the scales first:
def ScaleBalancing(strArr): 
    two_sides = list(map(int, strArr[0][1: -1].split(', ')))
    scale_list = sorted(list(map(int, strArr[1][1:-1].split(', ')))) 

    diff = abs(two_sides[0] - two_sides[1])
    
    seen = set()
    list_result = []
    
    for a in scale_list:
      if a == diff:
        return str(a)

      if a - diff in seen:
        return '{},{}'.format(a - diff, a)
      
      if diff - a in seen:
        return '{},{}'.format(*sorted([a, diff - a])) 
      
      seen.add(a)
      
    return "not possible"


print(ScaleBalancing( ["[6, 2]", "[1, 10, 6, 5]"]))

print(ScaleBalancing( ["[6, 1]", "[1, 10, 6, 5]"]))

