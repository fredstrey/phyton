i1,i2,i3=0,0,0
l1,l2,l3=[],[],[]
m=[]
matriz=[]
while i1 < 3:
    print("digite o " + str(i1+1) +" termo da primeira linha")
    l1.append(float(input()))
    i1+=1
while i2 < 3:
    print("digite o " + str(i2+1) +" termo da segunda linha")
    l2.append(float(input()))
    i2+=1
while i3 < 3:
    print("digite o " + str(i3+1) +" termo da terceira linha")
    l3.append(float(input()))
    i3+=1

matriz= [l1,l2,l3]
print(matriz)

l=matriz
d=[]
det=0
for i in l:
    for j in i:
        d.append(j)
print(d)
det = (d[0]*d[4]*d[8]) + (d[1]*d[5]*d[6]) + (d[2]*d[3]*d[7]) - (d[2]*d[4]*d[6]) - (d[0]*d[5]*d[7]) - (d[1]*d[3]*d[8])
print(str(det))
