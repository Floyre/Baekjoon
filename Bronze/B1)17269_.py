import sys
a = []
b = []
combi = []
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
strokes = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
alphabet_strokes = dict(zip(alphabets, strokes))

# 출력하여 확인
print(alphabet_strokes)

n, m = map(int,(sys.stdin.readline().split())) #name length
a, b = list(sys.stdin.readline().split())
a_stroke = []
b_stroke = []

for i in a:
    # 현재 글자가 알파벳 딕셔너리에 존재하는지 확인 / 루프를 돌면서 a의 알파뱃을 한개씩 할당
    if i in alphabet_strokes:
        # 알파벳에 해당하는 스트로크 숫자를 찾아 리스트에 추가
        stroke_number = alphabet_strokes[i]
        a_stroke.append(stroke_number)

for j in b:
    # 현재 글자가 알파벳 딕셔너리에 존재하는지 확인
    if j in alphabet_strokes:
        # 알파벳에 해당하는 스트로크 숫자를 찾아 리스트에 추가
        stroke_number = alphabet_strokes[j]
        b_stroke.append(stroke_number)

if(len(a) > len(b)):
    compare = 1
elif(len(a) < len(b)):
    compare = 2
    

# 딕셔너리(dictionary)와 zip함수에 대해 알게 되었다.

# dict는 파이썬의 내장 함수 중 하나로, 딕셔너리(dictionary)를 생성하는 데 사용됩니다. 
# 딕셔너리는 키(key)와 값(value)의 쌍을 항목으로 가지는 컬렉션 타입입니다. dict 함수는 여러 가지 방식으로 딕셔너리를 생성할 수 있으며, 키와 값을 매핑하는 데 사용됩니다.

# zip 함수는 두 개 이상의 반복 가능한(iterable) 객체들(예: 리스트, 튜플, 문자열 등)을 인자로 받아, 동일한 인덱스를 가진 요소들을 묶어서 튜플의 형태로 반환합니다. 
# 반환되는 결과는 zip 객체이며, 이는 반복자(iterator) 형태입니다. 보통 list, tuple 등으로 변환하여 사용합니다.