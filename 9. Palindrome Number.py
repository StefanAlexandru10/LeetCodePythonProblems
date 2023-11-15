x = 121
checker = str(x)
reverse = checker[::-1]

if int(reverse) == x:
    print("This is a palindrome")
else:
    print("This is not a palindrome")
