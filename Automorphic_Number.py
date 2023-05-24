n=int(input())
a=len(str(n))
sq=n**2
ld=sq%(10**a)
if ld==n:
    print("Automorphic Number");
else:
    print("Not an Automorphic Number");