cut_list = []

#Part 1
with open('input.txt') as f:
    for line in f:
        cut = {}
        at_symbol = line.find('@')
        comma_symbol = line.find(',')
        colon_symbol = line.find(':')
        x_symbol = line.find('x')
        cut['id'] = int(line.strip('#')[:at_symbol - 2])
        cut['left_coord'] = int(line[at_symbol + 2:comma_symbol]) + 1
        cut['top_coord'] = int(line[comma_symbol + 1:colon_symbol]) + 1
        cut['width'] = int(line[colon_symbol + 2:x_symbol])
        cut['height'] = int(line[x_symbol + 1:].rstrip('\n'))
        cut_list.append(cut)

fabric = [[0] * 1000 for _ in range(1000)]

for cut in cut_list:
    for x in range(cut['left_coord'], (cut['left_coord'] + cut['width'])):
        for y in range(cut['top_coord'], (cut['top_coord'] + cut['height'])):
            fabric[x-1][y-1] += 1

two_or_more = 0
for y in fabric:
    for x in y:
        if x >= 2:
            two_or_more += 1
print(f'How many square inches of fabric are within two or more claims?  {two_or_more}')


#Part 2
for cut in cut_list:
    overlap = False
    for x in range(cut['left_coord'], (cut['left_coord'] + cut['width'])):
        for y in range(cut['top_coord'], (cut['top_coord'] + cut['height'])):
            if fabric[x-1][y-1] > 1:
                overlap = True
    if overlap == False:
        print(f"The non-overlapping fabric is #{cut['id']}")