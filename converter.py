# this script converts the digits of pi to integers from a file to a new file
# example:
# 141592653589 in binary is 10000011110111100101000110111100010101
# new line every 4 characters:
# 1000
# 0011
# 1101
# 1110
# etc...
# these binary numbers are then converted into decimal numbers, for example:
# 8
# 3
# 13
# 14
# etc...

SEP = 4

# input file, this one starts with a '3.' which I omitted, you need to remove it if you
# chose to use another file
with open('pi-1mil.txt', 'r') as f:
    s = f.read().replace('\n', '')[2:]

# turn the digits into a string or binary numbers
d = '{0:b}'.format(int(s))
# add newlines every 'SEP'th characters
d = '\n'.join([str(int(d[i:i+SEP], 2)) for i in range(0, len(d), SEP)])

# write to file
with open(f'converted_{SEP}.txt', 'w') as f:
    f.write(d)