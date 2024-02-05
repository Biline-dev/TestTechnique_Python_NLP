def solution(N):
    power = 0
    while N % 2 == 0:
        N = N // 2
        power += 1
    
    return power


N = 1024
result = solution(N)
print(result)  # 10
