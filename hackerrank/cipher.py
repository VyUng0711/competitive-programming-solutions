# https://www.hackerrank.com/challenges/cipher/problem

n, k = map(int, input().split())
s = input()
l = len(s)
decoded = [0 for i in range(l)]
# The first digit is not XOR with anything
decoded[0] = int(s[0])
# Complexity: O(len(s))
for i in range(1, l):
    # To guess the digit at i, 
    # We know that decoded[i - 2] ^ decoded[i - 1] ^ decoded[i] = s[i]
    # when decoded[i - 2] ^ decoded[i - 1] = s[i - 1]
    # Therefore to generalize, s[i - 1] ^ decoded[i] = s[i]
    # This is equivalent to decoded[i] = s[i - 1] ^ s[i]

    decoded[i] = int(s[i - 1]) ^ int(s[i])
    # When i >= k, there is no longer shifting, and if we 
    # follow the same formula, there would be a redundant XOR with decoded[i - k]
    # therefore, we do another XOR with decoded[i - k] to balance this out (0)
    if i >= k:
        decoded[i] = decoded[i] ^ decoded[i - k]

res = "".join([str(x) for x in decoded[: l - k + 1]])
print(res)



