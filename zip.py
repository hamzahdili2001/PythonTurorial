# in zip The smoll obj it Controll All list obj

list1 = [1, 2, 3, 4, 5]
list2 = ['A', 'B']
list3 = [3, 4, 5, 6]
zipping = zip(list1, list2, list3)

print(zipping)
# <zip object at 0x7f2e90c3fc40>

for i in zipping:
    print(i)
# (1, 'A', 3)
# (2, 'B', 4)


