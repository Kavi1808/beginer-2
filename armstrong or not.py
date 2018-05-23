num=135
order=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10
    if num==sum:
        print(num,"armstrong")
    else:
        print(num,"not armstrong")
