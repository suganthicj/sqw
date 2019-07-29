    
x11,y11=map(int,input().split())
s=max(x11,y11)
for p in range(1,s):
	if x11%p==0 and y11%p==0:
		d=p
if x11==1 and y11==1:
    d=1
print(d)
