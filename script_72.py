
[2026-04-25 11:34:12.070866]
def factorial(n): return 1 if n==0 else n*factorial(n-1)

# 2026-05-01 05:07:19.624492
def is_palindrome(s):
    return s == s[::-1]


# 2026-07-24 00:29:17.390464
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


# 2026-08-06 10:15:17.867152
def is_palindrome(s):
    return s == s[::-1]


# 2026-09-16 01:18:00.574271
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1

