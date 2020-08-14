def reverse(num):
    IsNegative = False
    if num < 0:
        IsNegative = True
        num *= -1
    s_num = str(num)
    s_num = s_num[::-1]
    r_int = int(s_num)
    if(IsNegative):
        r_int *= -1

    if r_int >= 2**31 - 1 or r_int <= -2**31:
        return 0

    return r_int
    
print(reverse(-1020000))

        