import numpy as np
from termcolor import colored

# length of each row
SEP = 4
# desired patten to find in decimal format
# this one represents the following:
# '██' = 1
# '  ' = 0
#   ██████ (7  or 0111)
# ████     (12 or 1100)
# ████████ (15 or 1111)
#   ██  ██ (5  or 0101)
TARGET_PATTERN_INT = np.array([
    7,
    12,
    15,
    5
])
# length of the pattern
PATTERN_LEN = len(TARGET_PATTERN_INT)
# name of converted digits file
FILENAME = f'converted_{SEP}.txt'

# turns decimal integers into binary strings of length SEP
# example: 7 -> '0111'
def intToStrBinary(n):
    return format(n, f'#0{SEP+2}b')[2:]

# converts binary strings to printable characters
# example: '0101' -> '  ██  ██'
def intToPattern(n, charOn='██', charOff='  '):
    return ''.join(charOn if c == '1' else charOff for c in intToStrBinary(n))

# converts an array of integers to a string of binary digits
# example: [7, 12, 15, 5] -> '0111\n1100\n1111\n0101'
def decimalArrayToStr(array, char=intToStrBinary):
    return '\n'.join([char(n) for n in array])

print('Target pattern:')
print(decimalArrayToStr(TARGET_PATTERN_INT, intToPattern))

# read the file which contains the digits of pi stripped
with open(FILENAME, 'r') as f:
    lines = f.readlines()
    # turn everything into integers
    lines = [int(line.strip()) for line in lines]

# 
for i in range(len(lines)):
    print(f'Line {i}', end='\r')
    
    # compare arrays
    # there might be a better way to do this but this works and is already fast enough imo
    if all(lines[i+r] == TARGET_PATTERN_INT[r] for r in range(PATTERN_LEN)):
        print(f'Found pattern at line {i}')
        # prints 2 lines before the found pattern in white
        print(decimalArrayToStr(lines[i-2:i], intToPattern))
        # prints the pattern in cyan
        print(colored(decimalArrayToStr(lines[i:i+PATTERN_LEN], intToPattern), 'cyan'))
        # prints 2 lines after the found pattern in white
        print(decimalArrayToStr(lines[i:i+2], intToPattern))
        print()
    
print()
print('Done')