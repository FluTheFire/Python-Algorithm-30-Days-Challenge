def longestCommonPrefix(strs):
    if strs == []: 
        return ""
        
    s1, s2 = min(strs), max(strs)
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]: 
        i += 1
    return s1[:i]
        

raw_list = ["flower","flow","flight"]
raw_list2 = ["dog","racecar","care"]
raw_list3 = []
raw_list4 = ["aa", "a"]
print(longestCommonPrefix(raw_list4))

