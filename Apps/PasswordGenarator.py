from random import choice


def passwordGen():
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    samll_Allp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    big_Allp = ['G', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
    sp_Allp = ['!', '@', '#', '$', '%', '&', '*', '+', '.']

    password = f'{choice(numbers)}{choice(samll_Allp)}{choice(big_Allp)}{choice(sp_Allp)}{choice(numbers)}{choice(samll_Allp)}{choice(big_Allp)}{choice(sp_Allp)}'

    print(password)
print("Hamza Done!!")

passwordGen()
