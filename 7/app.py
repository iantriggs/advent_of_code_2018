unordered_steps = []
unique_steps = set()

with open('test_input.txt') as f:
    for line in f:
        # Step [0] must be done before [1]
        step = {}
        step[line[5]] = line[36]
        unordered_steps.append(step)
        unique_steps.add(line[5])
        unique_steps.add(line[36])

