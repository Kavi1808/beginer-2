def substrings(s):
  l = len(s)
  for a in range(l, 0, -1):
    for i in range(l-a+1):
      yield s[i: i+a]
def palindrome(s):
  return s == s[::-1]
def b(a):
    for l in substrings(a):
        if palindrome(l):
            return l
print b("malayalam")
