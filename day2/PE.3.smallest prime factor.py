n=600851475143



def prime_fact(n):
    if n>=2:
        for i in range(2,int(pow(n,0.5))):
            if n%i==0:
                return i
        return n



while True:
    prime_factor=prime_fact(n)
    if n>prime_factor:
        n=n//prime_factor
    else:
         print(n)
         break







                       
