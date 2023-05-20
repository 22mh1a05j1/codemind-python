p,r,t=map(int,input().split())
a=(1+r/100)**t;
b=p*a;
print("%.2f"%(b));