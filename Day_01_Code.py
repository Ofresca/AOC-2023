import re

input = open("2023\\Day_01_Input.txt",'r').read().split('\n')
tinput = open("2023\\Day_01_Test.txt",'r').read().split('\n')

result = 0

nmbrList = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

p1 = 0
p2 = 0

for line in input:
    p1_nmbrs = []
    p2_nmbrs = []
    for i, c in enumerate(line):
        if c.isdigit():
            p1_nmbrs.append(c)
            p2_nmbrs.append(c)
            continue
        for j,val in enumerate(nmbrList):
            if line[i:].startswith(val):
                p2_nmbrs.append(str(j+1))
                break
    p1+= int(p1_nmbrs[0]+p1_nmbrs[-1])
    p2+= int(p2_nmbrs[0]+p2_nmbrs[-1])
             
print('Result of Part 1: ', p1)
print('Result of Part 2: ', p2)

# for line in input:
#     first = 0
#     fl = 0
#     last = 0
#     i = 0
#     j = len(line)-1
#     while fl == 0 or last == 0:
#         if fl == 0:
#             print('i', i, line[i:i+2], line[i:i+3], line[i:i+4])
#             if str.isdigit(line[i]):
#                 fl = str(line[i]) 
#             elif line[i:i+3] == 'one':
#                 fl = '1'
#             elif line[i:i+3] == 'two':
#                 fl = '2'
#             elif line[i:i+5] == 'three':
#                 fl = '3'    
#             elif line[i:i+4] == 'four':
#                 fl = '4'
#             elif line[i:i+4] == 'five':
#                 fl = '5'    
#             elif line[i:i+3] == 'six':
#                 fl = '6'
#             elif line[i:i+5] == 'seven':
#                 fl = '7'    
#             elif line[i:i+5] == 'eight':
#                 fl = '8'
#             elif line[i:i+4] == 'nine':
#                 fl = '9'
#             print('first',fl, line, i)
#         i += 1 

#         if last == 0:
#             if str.isdigit(line[j]):
#                 last = str(line[j])
#             elif line[j-2:j+1] == 'one':
#                 last = '1'
#             elif line[j-2:j+1] == 'two':
#                 last = '2'
#             elif line[j-4:j+1] == 'three':
#                 last = '3'    
#             elif line[j-3:j+1] == 'four':
#                 last = '4'
#             elif line[j-3:j+1] == 'five':
#                 last = '5'    
#             elif line[j-2:j+1] == 'six':
#                 last = '6'
#             elif line[j-4:j+1] == 'seven':
#                 last = '7'    
#             elif line[j-4:j+1] == 'eight':
#                 last = '8'
#             elif line[j-3:j+1] == 'nine':
#                 last = '9' 
#             print('last', last, line, j)
#         j -= 1
#     print(int(str(fl) + str(last)))
    
#     result += int(str(fl) + str(last))

# print(result)