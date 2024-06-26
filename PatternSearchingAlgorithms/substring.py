def countVowelSubstrings(word):
    vowels = set('aeiou')
    n = len(word)
    count = 0
    
    for i in range(n):
        if word[i] in vowels:
            seen_vowels = set()
            for j in range(i, n):
                if word[j] in vowels:
                    seen_vowels.add(word[j])
                    if len(seen_vowels) == 5:
                        count += 1
                else:
                    break
    
    return count
    
print(countVowelSubstrings("cuaieuouac"))

# https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/
# A substring is a contiguous (non-empty) sequence of characters within a string.

# A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

# Given a string word, return the number of vowel substrings in word.

 

# Example 1:

# Input: word = "aeiouu"
# Output: 2
# Explanation: The vowel substrings of word are as follows (underlined):
# - "aeiouu"
# - "aeiouu"
# Example 2:

# Input: word = "unicornarihan"
# Output: 0
# Explanation: Not all 5 vowels are present, so there are no vowel substrings.