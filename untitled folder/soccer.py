import sys

data = sys.stdin.readline().strip()
inputlist = []
while True:
    inputlist.append(data)
    data = sys.stdin.readline().strip()
    if data == '':
        break

scores = {}
for i in inputlist:
    splitlist = i.split()
    name1 = splitlist[0][0]
    name2 = splitlist[0][2]
    scores1 = int(splitlist[1][0])
    scores2 = int(splitlist[1][2])
    if name1 not in scores.keys():
        scores[name1] = 0
    if name2 not in scores.keys():
        scores[name2] = 0

    if scores1 > scores2:
        scores[name1] = scores[name1] + 3
    elif scores1 == scores2:
        scores[name1] = scores[name1] + 1
        scores[name2] = scores[name2] + 1
    elif scores1 < scores2:
        scores[name2] = scores[name2] + 3

result = sorted(scores.items(), key=lambda x: (-x[1], x[0]))

for j in result:
    if j != result[-1]:
        print(*j, end=',')
    else:
        print(*j)

