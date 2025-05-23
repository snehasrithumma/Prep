def isSubsequence(s, t):
    m, n = len(s), len(t)
    i, j = 0, 0
    
    while i < m and j < n:
        if s[i] == t[j]:
            i += 1
        j += 1
    
    return i == m

print(isSubsequence('abc','ahbgdc'))

# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 