t=int(input())
ans=[]
for i in range(t):
    n,w=map(int,input().split())
    sum=0
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    for j in range(0,len(a)):
        sum+=a[j]
        if(sum>=w):
            ans.append(len(a)-j-1)
            break


for i in ans:
    print(i)
            
    
    
    
