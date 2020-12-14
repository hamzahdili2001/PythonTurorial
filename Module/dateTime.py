# This Module Can Handle Date And Time
import datetime

# print(dir(datetime.datetime)) # Show The Options In Module

print(datetime.datetime.now())

print('#' * 40)

# Get Current Year :
print(datetime.datetime.now().year)  # .year - month - hour - minute

print('#' * 40)

print(datetime.datetime.now().max)  # max = The End Of Time , min = Opesit

print('#' * 40)

print(datetime.datetime.now().time())  # Get The Current Time .
# .minute - second - hour and min - max
print(datetime.datetime.now().time().minute)
print('#' * 40)

# Custimaze date :
print(datetime.datetime(2001, 1, 1))

# Calc :

myBirthday = datetime.datetime(2001, 1, 1)
dateNow = datetime.datetime.now()
print(f'My Birthday is {myBirthday}')
print(f'Date Now is {dateNow}')

print(f'I Lived For {dateNow - myBirthday}')
print(f'I Lived For {(dateNow - myBirthday).days} Days .')

print('#' * 40)

myBirthday = datetime.datetime(2001, 1, 1)
print(myBirthday)

# Search in Google About 'strftime directive'
print(myBirthday.strftime('%d - %B'))
