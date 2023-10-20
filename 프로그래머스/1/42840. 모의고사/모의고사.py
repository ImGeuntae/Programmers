import math
def solution(answers):
    answer = []
    ans_list = []
    ans_list.append([1,2,3,4,5])
    ans_list.append([2,1,2,3,2,4,2,5])
    ans_list.append([3,3,1,1,2,2,4,4,5,5])
    score = [0,0,0]
    for i in range(3):
        ans = ans_list[i]*math.ceil(len(answers)/len(ans_list[i]))
        for j in range(len(answers)):
            if ans[j] == answers[j]:
                score[i] += 1
    max_score = max(score)
    while (max_score == max(score)):
        answer.append((score.index(max_score))+1)
        score[score.index(max_score)] = -1
    return answer