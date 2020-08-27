def romanToInt(s):
    roman_value = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    result = 0
    prev = 0
    
    for x in s:
        curr = roman_value[x]
        result += curr
        if curr > prev:
            result -= 2*prev
        prev = curr
    
    return result

print(romanToInt('IX'))

"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""