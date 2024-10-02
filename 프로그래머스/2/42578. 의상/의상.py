from collections import defaultdict

def solution(clothes):
    category_count = defaultdict(int)
    
    # 옷의 카테고리별 개수를 계산
    for _, category in clothes:
        category_count[category] += 1
    
    # 모든 카테고리에 대해 '입지 않는 경우(1)'를 포함하여 계산
    answer = 1
    for count in category_count.values():
        answer *= (count + 1)
    
    # 아무것도 입지 않는 경우를 제외
    return answer - 1