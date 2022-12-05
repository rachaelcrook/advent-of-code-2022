# text_file = open("day_4_input_test.txt", "r")
text_file = open("day_4_input.txt", "r")


def create_list(r1, r2):
    return [item for item in range(r1, r2+1)]

data = text_file.read()
split_data = data.split('\n')
# print(split_data)
pairs = 0
for string in split_data:
    first_string = string.split(',')
    first_part_string = list(map(int, first_string[0].split('-')))
    second_part_string = list(map(int, first_string[1].split('-')))
    first_start, first_end = first_part_string[0], first_part_string[1]
    second_start, second_end = second_part_string[0], second_part_string[1]
    section_one = create_list(first_start, first_end)
    section_two = create_list(second_start, second_end)
    # print(f'{section_one}  {section_two}')
    # check_one = all(item in section_one for item in section_two)
    # check_two = all(item in section_two for item in section_one)
    check_one = any(item in section_one for item in section_two)
    check_two = any(item in section_two for item in section_one)
    if check_one:
        pairs += 1
        # print(f'section two{section_two} was found in section one: {section_one}')
    if check_two and not check_one:
        pairs += 1
        # print(f'section one{section_one} was found in section two: {section_two}')

print(pairs)


text_file.close()





