scores = []
marks = []
for _ in range(int(input())):
	name = input()
	score = float(input())
	marks.append([name,score])
	scores.append(score)


second_lowest_mark = sorted(list(dict.fromkeys(scores)))[1]

for name,marks in sorted(marks):
	if marks == second_lowest_mark:
		print(name)



