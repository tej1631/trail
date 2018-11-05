a=[1,2,3,4,8,10,12]
b=[1,3,5,6,8]
k=len(a)
m=len(b)
c=[]
for i in range (k):
    for j in range (m):
        if a[i]==b[j]:
            print()
            c.append(a[i])
print(c)
    
