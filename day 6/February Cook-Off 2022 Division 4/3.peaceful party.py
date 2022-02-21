t=int(input())
ans=[]
for i in range(t):
    n=list(map(int,input().split()))
    if(n[0]+n[2]>n[1]):
        ans.append(n[0]+n[2])
    else:
        ans.append(n[1])
for i in ans:
    print(i)
