#isCurzon(5) ➞ True
# 2 ** 5 + 1 = 33
# 2 * 5 + 1 = 11
# 33 is a multiple of 11

def is_Curzon(num):
    x = 2 ** num+1
    y =2 * num+1
    if x%y == 0:
        return True
    else:
        return False

print(is_Curzon(5))
print(is_Curzon(10))
print(is_Curzon(14))