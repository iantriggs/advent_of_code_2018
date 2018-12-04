import string
alphabet = string.ascii_lowercase
results = []
reps = {}

# Section 1
with open('input.txt') as f:
    for line in f:
        temp_results = {}
        for char in line:
            if char not in temp_results:
                temp_results[char] = 1
            else:
                temp_results[char] += 1
        results.append(temp_results)

for result in results:
    for num in list(set(result.values())):
        if num not in reps:
            reps[num] = 1
        else:
            reps[num] += 1

checksum = 1
reps.pop(1)
for num in reps.values():
    checksum = checksum * num
print(f'The checksum is {checksum}')

box_list = []

# Section 2
box_names = []
with open('input.txt') as f:
    for line in f:
        box_list.append(line)


    for box in box_list:
        compare_box_list = box_list
        compare_box_list.remove(box)
        for compare_box in compare_box_list:
            differing_letters =  0
            for letter1, letter2 in zip(box, compare_box):
                if letter1 != letter2:
                    differing_letters += 1
            if differing_letters == 1:
                box_names.append(box)
                box_names.append(compare_box)

result_string = ''
for letter1, letter2 in zip(box_names[0], box_names[1]):
    if letter1 == letter2:
        result_string += letter1
print(result_string)