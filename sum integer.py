s=list()
k=3
n=input("enter the number you want:")
print ("enter the number:")
for i in range(int(n)):
  n=input("number:")
  s.append(int(n))
print("array:")
print(sum(s[0:k]))
