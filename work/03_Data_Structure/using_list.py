#! /usr/bin/env python3

# Это мой список покупок
shoplist = ['яблоки', 'манго', 'морковь','бананы']

print('Я должен сделать ', len(shoplist), 'покупок.')

print('Покупки:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nТак же нужно купить риса. ')
shoplist.append('рис')
print('Теперь мой список покупок таков:', shoplist)

print('Отсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный список покупок выглядит так:', shoplist)

print('Первое, что нужно купить, это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Я купил', olditem)
print('Теперь мой список покупок', shoplist)