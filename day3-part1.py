# text_file = open("day_3_input_test.txt", "r")
text_file = open("day_3_input.txt", "r")

data = text_file.read()
split_data = data.split('\n')
# print(split_data)
same = []
chars_as_nums = []
# print(split_data)
for s in split_data:
    temp_set = set()
    # print(s)
    first_half_string = s[:len(s)//2]
    second_half_string = s[len(s)//2:]
    # print('Full String: ' + s + ' First Half:' + first_half_string + ' Second Half:' + second_half_string)
    # print(first_half_string + '\n' + second_half_string)
    f_len = len(first_half_string)
    s_len = len(second_half_string)

    for first in first_half_string:
        for second in second_half_string:
            if first == second:
                temp_set.add(second)
                # print('Full String: ' + s + ' First Half:' + first_half_string + ' Second Half:' + second_half_string
                #       + ' Occurs in both: ' + second)
                # same.add(second)
    for item in temp_set:
        same.append(item)

for char in same:
    if char.islower():
        chars_as_nums.append(ord(char) - 96)
        # print(ord(char) - 96)
    if char.isupper():
        chars_as_nums.append(ord(char) - 38)
        # print(ord(char) - 38)


print(sum(chars_as_nums))
# print(chars_as_nums)
# print(same)
text_file.close()

