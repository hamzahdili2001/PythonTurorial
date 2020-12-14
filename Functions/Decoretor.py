
def myDecoretor(func):
    def function():
        print('Before')  # Just A msg
        func()  # The Function Decoretor
        print('After')  # Just A msg
    return function

@myDecoretor  # This The Deco
def Hello_World():
    print('HEllo World')  # This is The Place Of Func


Hello_World()

###################################
print('#' * 20)


def decor(func):

    def fun2(num1, num2):

        if num1 == 12 and num2 == 10:
            print('Hello World')
        else:
            func(num1, num2)



    return fun2
# @myDecoretor -> You can Add 2 Decoretor Or More

@decor
def calcNum(n1, n2):
    print(n1 + n2)


calcNum(12, 10)  # TThis is return Hello World
calcNum(10, 10)  # this is calc The Numbers

# ============================================================
# def deco(value):
#     def snippet(fname, lname):
#         if fname == 'Hamza' and lname == "Hdili":
#             print(f"Hello {fname} {lname} How Are You ")
#         else:
#             value(fname, lname)
#             print('Your Name Dos Not exist')
#     return snippet

# @deco
# def get_info(firstname, lastname):

#     print(f'Not Registerd.. {firstname} {lastname}')

# get_info('hamza', 'hdili')
# ============================================================
