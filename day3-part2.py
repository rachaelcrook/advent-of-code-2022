from itertools import islice

# text_file = open("day_3_input_test.txt", "r")
text_file = open("day_3_input.txt", "r")

data = text_file.read()
split_data = data.split('\n')
# print(split_data)
same = []
chars_as_nums = []
len_data = len(split_data)

for start in range(0, len_data, 3):
    end = start+3
    # print(f'Start: {start} End: {end}')
    elf_group = split_data[start:end]

    first = elf_group[0]
    second = elf_group[1]
    third = elf_group[2]

    temp_set = set()
    temp_set_compare = set()

    for f in first:
        for s in second:
            if f == s:
                temp_set_compare.add(s)

            for t in third:
                for i in temp_set_compare:
                    if t == i:
                        temp_set.add(t)

    # print(temp_set)
    for item in temp_set:
        same.append(item)
                # print('Full String: ' + s + ' First Half:' + first_half_string + ' Second Half:' + second_half_string
                #       + ' Occurs in both: ' + second)
                # same.add(second)
    # print(elf_group)


for char in same:
    if char.islower():
        chars_as_nums.append(ord(char) - 96)
        # print(ord(char) - 96)
    if char.isupper():
        chars_as_nums.append(ord(char) - 38)
        # print(ord(char) - 38)


print(sum(chars_as_nums))
print(chars_as_nums)
print(same)
text_file.close()

