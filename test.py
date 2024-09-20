# Given string and pattern
# string = "BBCBCBBCAACABBACCCBCBCABBACBCACBCCBACACCCCABBCCCCABACAABBCAACACBABBACACBBBCABBABCAABCCCBABAAAAABBCBBCABABAAABCCCCACBBBCAABCBCBABCBCBABAACBCCCACAAABCCCCCABBAABACAACCABCBABACBBACCCCCAACBBBCBAACACCACAAAC"
string = "BBCBCB"
pattern = "ABC"

pattern_length = len(pattern)
total_match_count = 0
for i in range(len(string) - pattern_length + 1):
    substring = string[i:i + pattern_length]
    print(substring)
    match_count = sum(1 for a, b in zip(substring, pattern) if a == b)
    total_match_count += match_count

# Count matches
print(f"The total number of matching letters between the substrings of the string and the pattern '{pattern}' is {total_match_count}.")