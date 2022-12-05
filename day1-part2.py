text_file = open("day_1_input.txt", "r")

data = text_file.read()
split_data = data.split('\n\n')

counter = 0
sum_list = []

for x in range(len(split_data)):
    counter += 1
    split_data_item = split_data[x]
    super_split_data = split_data_item.split('\n')
    sum_data = sum(map(int, super_split_data))
    sum_list.append(sum_data)

# max_value = max(sum_list)
top_three_values = sorted(sum_list, reverse=True)[:3]
sum_top_three = sum(top_three_values)
print(sum_top_three)

text_file.close()

