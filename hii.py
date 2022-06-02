records={}
for i in range(int(input())):
    name = input()
    score = float(input())
    records[name]=score

score=[float(i) for i in records]
print(score)