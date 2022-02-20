def SOE(n):
    PRIME=[True if x>1 else False for x in range(n+1)]
    #print(primes)
    p=2
    while(p*p<=n):
        if(PRIME[p]):
            for i in range(p**2,n+1,p):
                PRIME[i]=False
        p+=1
    PRIMES=[x for x in range(len(PRIME))if PRIME[x]]
    return PRIMES


PRIME=SOE(1999999)

print(sum(PRIME))
