k=bin(0xa10f4708c621be73)
print(k)
print(k[2:])
k=list(k[2:])
# for i in range(63,0,-8):    
#     k.pop(i)
# print(''.join(k))

n=57
i=1
pc1=[]

ex=list(range(1,100))

while len(pc1)!=56:
    if n<0:
        n=57+i
        i+=1
    pc1.append(ex[n-1])
    if n==36:
        n=63
        continue
    if n==7:
        n=62
        continue
    if n==5:
        n=28
        continue
    n-=8

res=[]
for i in range(0,56):
    res.append(k[pc1[i]-1])

print(pc1)
print(len(pc1))
print(''.join(res))
c=res[1:28]+list(res[0])+res[29:64]+list(res[28])
print(''.join(c))
print(len(c))
pc2=list(c[13])+list(c[16])+list(c[10])+list(c[23])+list(c[0])+list(c[4])+list(c[2])+list(c[27])+list(c[14])+list(c[5])+list(c[20])+list(c[9])+list(c[22])+list(c[18])+list(c[11])+list(c[3])+list(c[25])+list(c[7])+list(c[15])+list(c[6])+list(c[26])+list(c[19])+list(c[12])+list(c[1])+list(c[40])+list(c[51])+list(c[30])+list(c[36])+list(c[46])+list(c[54])+list(c[29])+list(c[39])+list(c[50])+list(c[44])+list(c[32])+list(c[47])+list(c[43])+list(c[48])+list(c[38])+list(c[55])+list(c[33])+list(c[52])+list(c[45])+list(c[41])+list(c[49])+list(c[35])+list(c[28])+list(c[31])
print(''.join(pc2))
print(len(pc2))
k2=hex(int(''.join(pc2),2))
print(k2)


