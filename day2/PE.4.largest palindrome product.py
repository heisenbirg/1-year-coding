ans=[]
for i in range(10,1000):
    for j in range(10,1000):
        if(str(i*j)==str(i*j)[::-1]):
            ans.append(i*j)



print(max(ans))
            
