import math

input = open("2023\\Day_02_Input.txt",'r').read().replace(',','').replace(';','').split('\n')
tinput = open("2023\\Day_02_Test.txt",'r').read().replace(',','').replace(';','').split('\n')

# Game 1: R, G, B; G, R, B; G, B

# Possible = 12 red, 13 green, 14 blue

# Need to check per line, per "" if each entry <= 12 red, <= 13 green, <= blue, 
# If true note Game number

p1 = 0
p2 = 0

MAX = {'red': 12, 'green': 13, 'blue': 14}

for game, line in enumerate(input): 
    items = line.split(' ')
    agame = game+1
    maxrgb = {key: 0 for key in MAX}
    for i in range(2, len(items)):
        if items[i] in maxrgb:
            if int(items[i-1]) > int(MAX[items[i]]):
                agame = 0
            if int(items[i-1]) > int(maxrgb[items[i]]):
                maxrgb[items[i]] = int(items[i-1])

    p1 += agame
    p2 += math.prod(maxrgb.values())

print('Part 1: ', p1)
print('Part 2: ', p2)

