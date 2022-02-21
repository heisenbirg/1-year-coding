t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    if(n==1):
        ans.append(6)
    elif(n==2):
        ans.append(5)
    elif(n==3):
        ans.append(4)
    elif(n==4):
        ans.append(3)
    elif(n==5):
        ans.append(2)
    elif(n==6):
        ans.append(1)


for i in ans:
    print(i)
