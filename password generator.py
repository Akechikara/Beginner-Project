# import random

# lower = 'abcdefghijklmnopqrstuvwxyz'
# upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# numbers = '0123456789'
# symbols = '@#$_-()_+'

# all = lower + upper + numbers + symbols

# length = int(input('Input your Password'))

# password = random.sample(all, length)
# password = ''.join(password)
# print(password)

import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()_+<>?|:;'

all = lower + upper + numbers + symbols

length = int(input('input your password'))

password = random.sample(all, length)
password = ''.join(password)
print(password)

