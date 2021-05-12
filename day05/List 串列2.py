import random as r
scores=[100,-10,90,80,999]
# error_scores=scores.pop(1)
# print(error_scores,scores)
# error_scores=scores.pop(3)
# print(error_scores,scores)

#利用POP () 將不合法的分數挑出
for x in scores:
    if x> 100 or x < 0:
        error_scores = scores.pop(scores.index(x))
print(scores)

#利用POP () 將不合法的分數挑出
scores1=[100,-10,90,-80,999]
ErrorScores=[]
for s in scores1:
    if s> 100 or s < 0:
        ErrorScores.append(s)
print(scores1)
print(ErrorScores)
for e in ErrorScores:
    scores1.pop(scores1.index(e))
print(scores1)

#反轉
scores=[1,7,3,5]
scores.reverse()
print(scores)

#排序
scores.sort()
print(scores)

#洗牌(請先 import random as r )
r.shuffleu(scores)
print(scores)
