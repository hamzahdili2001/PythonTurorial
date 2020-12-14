import random


def hamzaHdili(name):
    # This is The Doc
    ''' This Function Say Hello '''
    print(f'Hello {hamza}')


print(dir(hamzaHdili))

# Show The Docs :
print('#' * 30)
print(hamzaHdili.__doc__)
print('#' * 30)
help(hamzaHdili)
print('#' * 30)
# show random Module Doc.
print(random.__doc__)
print('#' * 30)
help(random.choices)
print(random.choice.__doc__)
