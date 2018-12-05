# Part 1
with open('input.txt') as f:
    units = f.read()
units = units[:-1]

def react(units):
    while True:
        matches = False
        for index, unit in enumerate(units):
            if index < (len(units) - 1):
                if abs(ord(unit) - ord(units[index + 1])) == 32:
                    matches = True
                    units = units.replace(f'{unit}{units[index + 1]}', '')
        if matches == False:
            break
    return units

shortlist = react(units)
print(f'The length is {len(shortlist)}')

# Part 2
letters = []
for char in shortlist:
    if char.lower() not in letters:
        letters.append(char.lower())
shortest = -1
for letter in letters:
    reduced_shortlist = shortlist.replace(letter, '').replace(letter.upper(), '')
    result = len(react(reduced_shortlist))
    if shortest == -1:
        shortest = result
    elif result < shortest:
        shortest = result
print(f'The shortest is {shortest}')