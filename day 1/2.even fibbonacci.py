n=int(input())
sum1=0
pre=1
nex=2
lst=[]

for i in range(n):
    sum1=pre+nex
    if sum1 <n:
        if sum1%2==0:
            lst.append(sum1)
        pre=nex
        nex=sum1
    else:
        break
print(sum(lst)+2)
