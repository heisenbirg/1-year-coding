t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    if n>65:
        ans.append('Overload')
    if n<35:
        ans.append('Underload')
for i in ans:
    print(i)
