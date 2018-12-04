import sys
current_frequency = 0
freq_tally = {}
freq_tally[0] = 1

# Section 1
with open('input.txt') as f:
    for line in f:
        current_frequency += int(line)
print(f'The total frequency is {current_frequency}')

# Section 2
current_frequency = 0
while True:
    with open('input.txt') as f:
        for line in f:
            current_frequency += int(line)
            if current_frequency in freq_tally.keys():
                print(f'The frequency repeated itself at {current_frequency}')
                sys.exit()
            else:
                freq_tally[current_frequency] = 1
