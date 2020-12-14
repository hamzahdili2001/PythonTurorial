# Hello This Code Create A Phone Numbers And Write The Numbers in A txt File
# i Choise The random Module To Get A Random Choices From The List 'numbers'
from random import choice


def getNum(num, countryKey):

    numbers = [x for x in range(10, 100)] 
    file = open('PhoneNum.txt', 'w')
    setp = set()  # The Set Remove The Repeated Numbers, That Way I Use It

    for n in range(num):
            # This is The Formatting Number
        get_number = f'{countryKey} {choice(numbers)}{choice(numbers)}-{choice(numbers)}{choice(numbers)} \n'
        setp.add(get_number)  # Adding The Numbers in The Set

    for i in setp:  # Writing The Number in The File.
        file.write(i)

    file.close()  # Closing The File

    print(f'{len(setp)} Phone Number Are Done!!')


getNum(30, '+2126')

# i Hope This Code Be Ease To Read
# You Cane Add The Number in DataBase Or csvFile Or Any File
