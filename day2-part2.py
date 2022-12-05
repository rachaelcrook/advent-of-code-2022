import pandas as pd

# Rock Paper Scissors Rules
# rock defeats scissors, scissors defeats paper, and paper defeats rock.
# If both players choose the same shape, the round ends in a draw

# How to decode strategy guide / A.K.A input file
# The first column is what your opponent is going to play
# A = Rock
# B = Paper
# C = Scissors
# The second column is how the round needs to end.
# X = you lose
# Y = draw
# Z = you win


df = pd.read_csv("day_2_input.txt", sep=" ", header=None)
# df = pd.read_csv("day_2_input_test.txt", sep=" ", header=None)

opponent_rock = df[0] == 'A'
opponent_paper = df[0] == 'B'
opponent_scissors = df[0] == 'C'

round_result_you_lose = df[1] == 'X'
round_result_draw = df[1] == 'Y'
round_result_you_win = df[1] == 'Z'

df.loc[opponent_rock, 0] = 'rock'
df.loc[opponent_paper, 0] = 'paper'
df.loc[opponent_scissors, 0] = 'scissors'

df.loc[round_result_you_lose, 1] = 'you lose'
df.loc[round_result_draw, 1] = 'draw'
df.loc[round_result_you_win, 1] = 'you win'

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
    round_result = game_round[1]

    if round_result == 'you lose' and opponent == 'rock':
        # my play is scissors, scissors=3, you lose=0, round total=3
        return 3
    elif round_result == 'you lose' and opponent == 'paper':
        # my play is rock, rock=1, you lose=0, round total=1
        return 1
    elif round_result == 'you lose' and opponent == 'scissors':
        # my play is paper, paper=2, you lose=0, round total=2
        return 2
    elif round_result == 'draw' and opponent == 'rock':
        # my play is rock, rock=1, draw=3, round total=4
        return 4
    elif round_result == 'draw' and opponent == 'paper':
        # my play is paper, paper=2, draw=3, round total=5
        return 5
    elif round_result == 'draw' and opponent == 'scissors':
        # my play is scissors, scissors=3, draw=3, round total=6
        return 6
    elif round_result == 'you win' and opponent == 'rock':
        # my play is paper, paper=2, you win=6, round total=8
        return 8
    elif round_result == 'you win' and opponent == 'paper':
        # my play is scissors, scissors=3, you win=6, round total=9
        return 9
    elif round_result == 'you win' and opponent == 'scissors':
        # my play is rock, rock=1, you win=6, round total=7
        return 7


df[2] = df.apply(calculate_score, axis="columns", result_type='expand')
print(df[2].sum())
print(df)
# text_file = open("day_2_input.txt", "r")
#
# data = text_file.read()
