import io
import re
import pandas as pd


# text_file = open("day_5_input_test.txt", "r")
text_file = open("day_5_input.txt", "r")
data = text_file.read()
crates_and_moves = data.split('\n\n')
instructions = crates_and_moves[1].splitlines()
crates = crates_and_moves[0]
result = re.sub(' +', ',', crates)
buffer = io.StringIO(result)
print(result)
df = pd.read_csv(filepath_or_buffer=buffer, sep=",", header=None, skipfooter=1,
                 engine='python', keep_default_na=False).to_dict('list')

for l in df:
    while ("" in df[l]):
        df[l].remove("")


print(f'Beginning Crate Stack: \n {df}')


for line in instructions:

    remove_letters = re.sub('[a-zA-Z]+', ' ', line)
    remove_whitespace = re.sub(' +', ' ', remove_letters)
    convert_to_list = remove_whitespace.split(' ')
    convert_to_list.pop(0)
    convert_list_to_int = list(map(int, convert_to_list))

    quantity_to_move = convert_list_to_int[0]
    subtract_from = convert_list_to_int[1] - 1
    column_to_add_to = convert_list_to_int[2] - 1

    print(f'Column to add to: {column_to_add_to} Quantity: {quantity_to_move}'
          f' Subtract From: {subtract_from}')

    for crate in range(0, quantity_to_move):
        item_to_add = df[subtract_from][0]
        item_to_remove = df[subtract_from]
        df[column_to_add_to].insert(0, item_to_add)
        item_to_remove.pop(0)
        # print(df)


print(f'Final Crate Stack: \n {df}')



text_file.close()

