print("insira o número de linhas e colunas da matriz (obs: so sei calcular determinante de matriz 2x2, 3x3 e 4x4)")
lc = int(input())
if lc < 2:
    print("não é uma matriz, burro!")
if lc > 4:
    print("eu so sei calcular determinante de matriz 2x2, 3x3 e 4x4!")
if lc== 3:
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
    print("o determinante da matriz e: " +str(det))
if lc ==4:
    i1,i2,i3,i4=0,0,0,0
    l1,l2,l3,l4=[],[],[],[]
    m=[]
    matriz=[]
    while i1 < 4:
        print("digite o " + str(i1+1) +" termo da primeira linha")
        l1.append(float(input()))
        i1+=1
    while i2 < 4:
        print("digite o " + str(i2+1) +" termo da segunda linha")
        l2.append(float(input()))
        i2+=1
    while i3 < 4:
        print("digite o " + str(i3+1) +" termo da terceira linha")
        l3.append(float(input()))
        i3+=1
    while i4 < 4:
        print("digite o " + str(i4+1) +" termo da quarta linha")
        l4.append(float(input()))
        i4+=1


    matriz= [l1,l2,l3,l4]
    print(matriz)

    l=matriz
    d=[]
    det=0
    for i in l:
        for j in i:
            d.append(j)
    print(d)
    det = d[0]*(d[5]*d[10]*d[15] + d[6]*d[11]*d[13] + d[7]*d[9]*d[14] - d[7]*d[10]*d[13] - d[6]*d[9]*d[15] - d[5]*d[11]*d[14])-d[1]*(d[4]*d[10]*d[15] + d[6]*d[11]*d[12] + d[7]*d[8]*d[14] - d[7]*d[10]*d[12] - d[6]*d[8]*d[15] - d[4]*d[11]*d[14])+d[2]*(d[4]*d[9]*d[15] + d[5]*d[11]*d[12] + d[7]*d[8]*d[13] - d[7]*d[9]*d[12] - d[5]*d[8]*d[15] - d[4]*d[11]*d[13])-d[3]*(d[4]*d[9]*d[14] + d[5]*d[10]*d[12] + d[6]*d[8]*d[13] - d[6]*d[9]*d[12] - d[5]*d[8]*d[14] -d[4]*d[10]*d[13])
    print("o determinante da matriz e: " +str(det))
if lc ==2:
    i1,i2=0,0
    l1,l2=[],[]
    m=[]
    matriz=[]
    while i1 < 2:
        print("digite o " + str(i1+1) +" termo da primeira linha")
        l1.append(float(input()))
        i1+=1
    while i2 < 2:
        print("digite o " + str(i2+1) +" termo da segunda linha")
        l2.append(float(input()))
        i2+=1
    matriz= [l1,l2]
    print(matriz)

    l=matriz
    d=[]
    det=0
    for i in l:
        for j in i:
            d.append(j)
    print(d)
    det = (d[0]*d[3] - d[1]*d[2])
    print("o determinante da matriz e: " +str(det))    
