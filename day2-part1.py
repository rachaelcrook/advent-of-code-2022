import pandas as pd

# Rock Paper Scissors Rules
# rock defeats scissors, scissors defeats paper, and paper defeats rock.
# If both players choose the same shape, the round ends in a draw

# How to decode strategy guide / A.K.A input file
# The first column is what your opponent is going to play
# A = Rock
# B = Paper
# C = Scissors
# The second column is what you should play in response
# X = Rock
# Y = Paper
# Z = Scissors


df = pd.read_csv("day_2_input.txt", sep=" ", header=None)
# df = pd.read_csv("day_2_input_test.txt", sep=" ", header=None)

opponent_rock = df[0] == 'A'
opponent_paper = df[0] == 'B'
opponent_scissors = df[0] == 'C'

my_play_rock = df[1] == 'X'
my_play_paper = df[1] == 'Y'
my_play_scissors = df[1] == 'Z'

df.loc[opponent_rock, 0] = 'rock'
df.loc[opponent_paper, 0] = 'paper'
df.loc[opponent_scissors, 0] = 'scissors'

df.loc[my_play_rock, 1] = 'rock'
df.loc[my_play_paper, 1] = 'paper'
df.loc[my_play_scissors, 1] = 'scissors'

# print(df)
# running_score = []

# Score for the round is relative to the shape you chose.
# rock = 1
# paper = 2
# scissors = 3
# plus the score for the outcome of the round
# you lost = 0
# draw = 3
# you won = 6


def calculate_score(game_round):
    opponent = game_round[0]
    my_play = game_round[1]

    # rock=1, draw=3, so round total = 4
    if my_play == 'rock' and opponent == 'rock':
        return 4
    # rock=1, you lost=0, so round total = 1
    elif my_play == 'rock' and opponent == 'paper':
        return 1
    # rock=1, you won=6, so round total = 7
    elif my_play == 'rock' and opponent == 'scissors':
        return 7
    # paper=2, you won=6, so round total = 8
    elif my_play == 'paper' and opponent == 'rock':
        return 8
    # paper=2, draw=3, so round total = 5
    elif my_play == 'paper' and opponent == 'paper':
        return 5
    # paper=2, you lost=0, so round total = 2
    elif my_play == 'paper' and opponent == 'scissors':
        return 2
    # scissors=3, you lost=0, so round total = 3
    elif my_play == 'scissors' and opponent == 'rock':
        return 3
    # scissors=3, you won=6, so round total = 9
    elif my_play == 'scissors' and opponent == 'paper':
        return 9
    # scissors=3, draw=3, so round total = 6
    elif my_play == 'scissors' and opponent == 'scissors':
        return 6


df[2] = df.apply(calculate_score, axis="columns", result_type='expand')
print(df[2].sum())
print(df)
# text_file = open("day_2_input.txt", "r")
#
# data = text_file.read()
