i=200
a=2
for n in range(2,i):
    count=0
    
    while(a!=1):
            if(a%2==0):
                    a=a/2
            else:
                    a=3*a+1
            count+=1
    a=n

    print(f'{n} count=',count+1)
