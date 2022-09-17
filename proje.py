# Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. 

liste1=[[1,'a',['cat'],2],[[[3]],'dog'],4,5,[1,2,3]]
liste2=[]
def duzlestir(x):
    for i in x:
        if type(i) == list:
            duzlestir(i)
        else:
            liste2.append(i)
    return liste2
print(duzlestir(liste1))


# Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün

liste1=[[1, 2], [3, 4], [5, 6, 7]]
liste2=[]
def tersdondur(y):
    for i in list(reversed(y)):
        liste2.append(list(reversed(i)))
    return print(liste2)
tersdondur(liste1)