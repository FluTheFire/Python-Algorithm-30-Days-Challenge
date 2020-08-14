def isPalindrome(x: int) :
    if x < 0 or (x > 0 and x%10 == 0):   # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
        print("Lol")
        return False
    
    result = 0
    while x > result:
        result = result * 10 + x % 10
        print(f"x % 10: {x % 10}")
        print(f"result: {result}")
        x = x // 10
        print(f"x: {x}")
        print("--------------------------------")
    
        
    return True if (x == result or x == result // 10) else False

num = 101

print(isPalindrome(num))
print("======================================================")

def isPalindrome_2(x: int):
    if x < 0 or (x > 0 and x%10 == 0):
        return False
    # print(str(x)[::-1] + ":" + str(x))
    # print('--------------------------------------------------')
    return str(x) == str(x)[::-1]

print(isPalindrome_2(num))