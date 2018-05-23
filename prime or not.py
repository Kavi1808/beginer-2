num=407
if num>1:
    for i in range(2,num):
        if(num%1)==0:
            print(num,"not prime")
            print(i,"times",num//i,"is",num)
        break
    else:
        print(num,"prime")
else:
    print (num,"not prime")      
