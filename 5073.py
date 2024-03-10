ans = []
while True:
        a,b,c = map(int, input().split())
        if a == b == c == 0:
            break
        elif a == b == c:
            ans.append("Equilateral")
        elif a == b != c or a == c != b or b == c != a:
            ans.append("Isosceles")
        elif a != b != c:
            temp = a + b + c
            temp -= (max(a, b, c))*2
            if temp <= 0:
                ans.append("Invalid")
            else:
                ans.append("Scalene")
for a in ans:
    print(a)