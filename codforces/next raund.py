import sys
numbers = [int(i) for i in sys.stdin.readline(). split()]

k = numbers[1]

scores = [int(i) for i in sys.stdin.readline().split()]

next_round_members = 0

for score in scores:
    if score >= scores[k - 1] and score != 0 :
        next_round_members += 1


print(next_round_members)