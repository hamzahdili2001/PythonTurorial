# Generator #
def generator():
    yield 1
    yield 2
    yield 3
    yield 4


myGen = generator()

print(next(myGen))  # 1
print(next(myGen))  # 2
print(next(myGen))  # 3


print('-' * 20)

for n in myGen:  # Get 4
    print(n)

################################################################
## iterator ##
print('-' * 20)
# iterator
myNum = [1, 2, 3, 4, 5]
num = iter(myNum)

print(next(num))
print(next(num))

print('-' * 20)
for i in num:
    print(i)
