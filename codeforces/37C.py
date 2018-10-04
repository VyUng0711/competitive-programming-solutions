# http://codeforces.com/contest/37/problem/C

# Method 1: Backtracking - Recursion
import sys
sys.setrecursionlimit(1000000)

      
def dfs (x, s):
  global count
  global done
  if x == sorted_a[count][1]:
    sorted_a[count][2] = s
    count += 1
    if count == num_words:
      done = True
    return
  dfs(x + 1, s + '0')
  if count == num_words:
    return
  dfs(x + 1, s + '1')
  
  
num_words = int(input())
word_lens = list(map(int, input().split()))

a = []
for i in range(num_words):
  a.append([i, word_lens[i], ""])
  #a[i] = Node(i, word_lens[i], "")

sorted_a = sorted(a, key=lambda x: x[1])
# print(sorted_a)
  
count = 0
done = False
  
dfs(0, "")
# done = dfs(sorted_a)

ordered_a = sorted(sorted_a, key=lambda x: x[0])
# print(ordered_a)
if not done:
  print("NO")
else:
  print("YES")
  for k in ordered_a:
    print(k[2])

# Method 2: Using trie and stack 
import sys
sys.setrecursionlimit(1000000)
class Node:
    def __init__(self, val):
        self.child = dict()
        self.is_blocked = False
        self.val = val
        
    def traversal(self, cur_str, res):
        if len(self.child) == 0:
            res.append((self.id, cur_str))
        if 0 in self.child:
            self.child[0].traversal(cur_str + '0', res)
        if 1 in self.child:
            self.child[1].traversal(cur_str + '1', res)

class Trie:
    def __init__(self):
        self.root = Node('*')
    
    def add(self, max_len, id):
        st = [self.root]
        while max_len and len(st):
            u = st[-1]
            max_len -= 1
            if 0 not in u.child:
                u.child[0] = Node(0)
            if not u.child[0].is_blocked:
                st.append(u.child[0])
            else:
                if 1 not in u.child:
                    u.child[1] = Node(1)
                if not u.child[1].is_blocked:
                    st.append(u.child[1])
                else:
                    u.is_blocked = True
                    max_len += 2
                    st.pop()
        if max_len == 0:
            st[-1].is_blocked = True
            st[-1].id = id
            return True
        return False
        
        
n = int(input())
a = list(map(int, input().split()))
a = [(a[i], i) for i in range(n)]
a.sort()

trie = Trie()
for x, i in a:
    if not trie.add(x, i):
        print('NO')
        exit()

print('YES')
res = []
trie.root.traversal('', res)
res.sort()

for i, s in res:
    print(s)
