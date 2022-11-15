#1.a) 
 
def inicDiferente(s1, s2):
    res=0
    for carater in s1:
        if carater not in s2:
            res=res+1
        else:
            return res 
    print(res)

#1.b)

def acimaMedia(n):
    lista=[]
    soma = 0
    res=0
    while n > 0:
        num = int(input("Introduza um número: "))
        lista.append(num)
        n= n-1
    for i in lista:
        soma = soma + i
    media = soma/len(lista)
    for i in lista: 
        if i > media:
            res = res+1
    return res

#1.c)

def merge(l1, l2):
    lista = l1+l2
    for i in range(len(lista)):
        i=1
        while i < len(lista):
            if lista[i]<lista[i-1]:
                lista[i],lista[i-1]=lista[i-1],lista[i]
            i=i+1
    return lista
    
#1.d)

def figuais(f1, f2):
    file1 = open(f1)
    file2 = open(f2)
    lista1 = []
    lista2=[]
    res = False
    for linha in file1:
        lista1.append(linha)
    for linha in file2:
        lista2.append(linha)

    print(lista1)
    print(lista2)
    if len(lista1)==len(lista2):
        for i in range(len(lista1)):
            if lista1[i]==lista2[i]:
                res = True
    else:
        resp = False
    file1.close()
    file2.close()
    return res
    
#2.a)

def atores(cinemateca):
    lista=[]
    for _,_,elenco,*_ in cinemateca:
        for ator in elenco:
            if ator not in lista:
                lista.append(ator)
    lista.sort()
    return lista

#2.b)

def listarPorGenero(cinemateca, genero):
    lista=[]
    for titulo,_,_,generofilme in cinemateca:
      for tipo in generofilme:
            if tipo==genero:
                  lista.append(titulo)
    lista.sort()
    return lista

#2.c)

def maiorElenco( cinemateca ):
    maior = 0
    for titulo,_,elenco,*_ in cinemateca:
        if len(elenco)>maior:
            maior = len(elenco)
            res = titulo
    return res

#2.d)

def filmePorGenero( cinemateca ):
    distrib = {}
    for _,_,_,genero in cinemateca:
        for tipo in genero:
            if tipo not in distrib.keys():
                distrib[tipo]=1
            else:
                distrib[tipo]+=1
    return distrib

#2.e)

def grafico(cinemateca):
    import matplotlib.pyplot as plt
    distrib = filmePorGenero(cinemateca)
    plt.bar(distrib.keys(), distrib.values(),color=["red"])
    plt.xticks([x for x in range(0, len(distrib.keys()))], distrib.keys(), rotation='vertical')
    plt.title("Distribuição de Filmes por Género")
    plt.xlabel("Géneros")
    plt.ylabel("Número de Filmes")
    plt.show()
    return