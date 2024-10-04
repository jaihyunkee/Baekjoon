def solution(routes):
    answers = []
    routes.sort()
    for route in routes:
        boo = False
        for i, rang in enumerate(answers):
            mi, ma = rang[0], rang[1]
            route_a, route_b = route[0], route[1]
            if mi <= route_a <= ma or mi <= route_b <= ma:
                from_ = max(route_a, mi)
                to_ = min(route_b, ma)
                answers[i] = [from_, to_]
                boo = True
        if not boo:
            answers.append(route)
            
    return len(answers)