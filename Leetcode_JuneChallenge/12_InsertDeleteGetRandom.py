h={}
j=['a','b','c','d','a']
s=[]
for i in range(len(j)):
    if j[i] not in h:
        h[i]=j[i]
    s.append(i)
print(h)

print(s)
a=[*h.keys()]x
print(a)