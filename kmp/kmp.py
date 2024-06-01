# Knuth-Morris-Pratt (KMP) algorithm is a string matching algorithm that efficiently 
# searches for occurrences of a "pattern" string within a "text" string. 
# It was designed to improve the time complexity of string searching, providing an efficient way to perform the task by 
# avoiding unnecessary comparisons.
def compute_lps(pattern):
    length = 0  # length of the previous longest prefix suffix
    lps = [0] * len(pattern)
    i = 1
    
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
                
    return lps

def kmp_search(text, pattern):
    m = len(text)
    n = len(pattern)
    
    lps = compute_lps(pattern)
    
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < m:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            
        if j == n:
            print(f"Found pattern at index {i - j}")
            j = lps[j - 1]
        elif i < m and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

text = "ababcababcababc"
pattern = "ababc"
kmp_search(text, pattern)


# String: "abab"

# Prefixes:

# "a"
# "ab"
# "aba"
# "abab" (not a proper prefix)
# Suffixes:

# "b"
# "ab"
# "bab"
# "abab" (not a proper suffix)
# Proper Prefixes (excluding the entire string):

# "a"
# "ab"
# "aba"
# Proper Suffixes (excluding the entire string):

# "b"
# "ab"
# "bab"
# Proper Prefixes that are also Suffixes:

# The proper prefix from the list above that is also a suffix is "ab".
# Longest Proper Prefix which is also a Suffix:
# The longest proper prefix which is also a suffix for the string "abab" is "ab".
# Summary:
# String: "abab"
# Prefixes: "a", "ab", "aba", "abab"
# Proper Prefixes: "a", "ab", "aba"
# Suffixes: "b", "ab", "bab", "abab"
# Proper Suffixes: "b", "ab", "bab"
# Longest Proper Prefix which is also a Suffix: "ab"


