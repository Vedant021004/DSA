s = "level"

s_rev = s[::-1]

i = 0

while i < len(s):

    if s[i] != s_rev[i]:
        print("Not a palindrome")
        break

    i += 1

else:
    print("Palindrome")