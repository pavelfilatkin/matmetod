#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Мы владельцы магазина игрушек. В начале каждого дня мы закупаем несколько игрушек по 50 руб.
# Цена реализации нашего продукта - 60 рублей за единицу.
# Из наблюдений известно, что спрос на этот продукт за день может быть равен 1,2,3 или 4 единицам.
# Пусть известно, что на практике спрос на 1 единицу наблюдался X раз, спрос на 2 единицы наблюдался Y раз, 
# спрос на 3 единицы наблюдался Z раз, спрос на 4 единицы наблюдался Q раз.
# Если продукт в течение дня не был распродан, то в конце дня мы его продавали друзьям из ближнего зарубежья 
# по цене 20 рублей за единицу. 


# In[100]:


import numpy as np
print('Введите кол-во стратегий для игры с природой: ')
n=int(input())
print("Каков был спрос для различных сценариев покупки товара?")
v1=[]
for i in range(1,n+1):
    print('Введите сколько раз купили',i,'единицы продукции')
    X=int(input())
    v1.append(X)
s=sum(v1)
for i in range(n):
    v1[i]/=s
print('Тогда вероятности наступления наших сценариев: ',*v1,sep='   ')


# In[101]:



# Функция для ввода данных пользователем с клавиатуры
print('Используем матрицу финансовых последствий')
print('Финансовые последствия = (кол-во проданных продуктов * цена продажи) - (кол-во закупленных продуктов * цена закупки)')
def reading_entering(n):
    matrix = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(int(input('Введите элемент матрицы финансовых последствий ')))
        matrix.append(temp)
    return matrix
matrix_a = reading_entering(n)
print('Ваша матрица финансовых последствий - ')
for i in range(n):
    print(matrix_a[i])


# In[102]:



#байес

a1=np.array(v1)
b1=np.array(matrix_a)
bayes=np.sum(a1*b1,axis=1)
print('Цена игры по критерию Байеса составляет: ',int(max(bayes)), "при выборе стратегии номер: ", list(bayes).index(max(bayes))+1)


#лаплас
v2=[0.25,0.25,0.25,0.25]
a2=np.array(v2)
laplas=np.sum(a2*b1,axis=1)
print('Цена игры по критерию Лапласа составляет: ',int(max(laplas)), "при выборе стратегии номер: ", list(laplas).index(max(laplas))+1)



#гермейер
G=[]
for i in range(n):
    g=[]
    for j in range(n):
        q=matrix_a[i][j]*v1[j]
        g.append(q)
    G.append(g) 
Gg=[]
for i in G:
    Gg.append(min(i))
print('Цена игры по критерию Гермейра составляет: ',int(max(Gg)),"при выборе стратегии номер: ", Gg.index(max(Gg))+1)

#оптимизм
O=[]
for i in matrix_a:
    O.append(max(i))
print('Цена игры по критерию оптимизма составляет: ',int(max(O)),"при выборе стратегии номер: ", O.index(max(O))+1)

#пессимизм и Вальда
P=[]
for i in matrix_a:
    P.append(min(i))
print('Цена игры по критерию пессимизма составляет: ',int(min(P)),"при выборе стратегии номер: ", P.index(min(P))+1)

print('Цена игры по критерию Вальда составляет: ',int(max(P)),"при выборе стратегии номер: ", P.index(max(P))+1)


#Гурвиц
print('Задайте ВАШ коэффициент готовности к риску от 0 до 10, где 0 - Вы шахматист, а 10 - Вы пилот болида Формулы 1')
k=int(input())/10
O1=[]
for i in matrix_a:
    O1.append(max(i))
P1=[]
for i in matrix_a:
    P1.append(min(i))
Gur=[]
for i in range(n):
    Gur.append(k*O1[i]+(1-k)*P1[i])
print('Цена игры по критерию Гурвица составляет: ',int(max(Gur)),"при выборе стратегии номер: ", Gur.index(max(Gur))+1)    


#сэвидж
S1=[]
s=np.array(matrix_a)
s=np.rot90(s,k=-1)

for i in s:
    S1.append(max(i))
s=np.rot90(s)
    
for i in range(n):
    for j in range(n):
        s[i][j]=S1[j]-s[i][j]
        
S2=[]
for i in s:
    S2.append(max(i))
print('Цена игры по критерию Сэвиджа составляет: ',int(min(S2)),"при выборе стратегии номер: ", S2.index(min(S2))+1)


# In[ ]:




