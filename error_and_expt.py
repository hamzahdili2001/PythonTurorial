# Errors And Exception - Raising

# num = -1

# if num < 0:

#     raise Exception(f'The number {num} Is less Than Zero')

#     print('This Will Not Print Because The Error')

# else:
#     print(f'{num} is Good')


################

num = 'hamza'

try:
    if 'hamza' == 10:
        print('Hamza')

except SyntaxError:  # ValueError - Exception ...
    print(f'{num} is Not A Number')

# The End
