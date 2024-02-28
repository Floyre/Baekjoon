# 첫 번째 줄에 OX표의 길이인 자연수 N이 주어진다. (1 ≤ N ≤ 10,000)
# 두 번째 줄에 OX표를 의미하는 문자열 S가 주어진다. S는 O(알파벳 대문자 O, ASCII 코드 79)와 X(알파벳 대문자 X, ASCII 코드 88)로만 구성되어 있으며, 길이는 N이다.
# 문자열 S의 i 번째 글자가 O이면 해당 참가자가 i 번째 문제를 맞혔음을 의미하고, X이면 틀렸음을 의미한다.

n = int(input())
quiz = list(input())
bonus = 0
score = 0
for i in range(len(quiz)):
    if(quiz[i] == "O"):
        bonus +=1
        score = score + i + bonus
    elif(quiz[i] == "X"):
        bonus = 0
print(score)