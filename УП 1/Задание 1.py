def numJewelsInStones(J, S):
    return sum(s in J for s in S)

J = "ab"
S = "aabbccd"

print(numJewelsInStones(J, S))
