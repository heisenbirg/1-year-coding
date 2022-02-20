f=0
for a in range(2,1000):
    if(not f):
        for b in range(3,1000):
            if(a**2+b**2==(1000-(a+b))**2):
                f=1
                print(a*b*(1000-(a+b)))
                break

