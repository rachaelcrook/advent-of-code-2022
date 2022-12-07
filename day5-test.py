import io
import os
import tempfile
import re
import pandas as pd
# tmp = tempfile.NamedTemporaryFile(mode='a+', delete=False)
# temp_file = open(tmp.name, 'w')
text_file = open("day_5_input_test.txt", "r")
data = text_file.read()
crates_and_moves = data.split('\n\n')

moves = crates_and_moves[1].splitlines()
crates = crates_and_moves[0]
result = re.sub(' +', ',', crates)

buffer = io.StringIO(result)
df = pd.read_csv(filepath_or_buffer=buffer, sep=",", header=None, skipfooter=1, engine='python')

print(df)


text_file.close()

